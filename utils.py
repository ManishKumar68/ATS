from dotenv import load_dotenv
import os
from PIL import Image
import pdf2image
import google.generativeai as genai
import io
import base64
import streamlit as st
import json

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get AI response
def get_gemini_response(input_text, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, pdf_content[0], prompt])
    return response.text

# Function to process PDF and extract first page as image
@st.cache_data(show_spinner=False)
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Convert PDF to image with lower resolution for faster processing
        images = pdf2image.convert_from_bytes(uploaded_file.read(), dpi=100)
        first_page = images[0]
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG', quality=85)
        img_byte_arr = img_byte_arr.getvalue()
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded. Please upload a PDF file.")

# Scoring function for resume
def score_resume(job_description, pdf_content):
    # Define a scoring prompt matching main.py
    scoring_prompt = """
    You are an HR expert analyzing a resume against a job description. Provide scores (0-100) for:
    1. Skills: Match of technical/soft skills to job requirements.
    2. Experience: Relevance and duration of work experience.
    3. Keywords: Presence of key terms from the job description.
    4. Formatting: ATS-friendliness and readability.

    Job Description: {job_description}


    Follow with a detailed breakdown of each score category, explaining the evaluation:
    - Skills: Describe the match of technical/soft skills to job requirements.
    - Experience: Evaluate relevance and duration of work experience.
    - Keywords: Assess presence of key terms from the job description.
    - Formatting: Analyze ATS-friendliness and readability.

    At the end, include scores as a JSON object: {{"Skills": X, "Experience": Y, "Keywords": Z, "Formatting": W}}
    Do not prepend scores with "Resume Scores:", numbered points, or any additional text or summary.
    """
    
    # Format the prompt
    formatted_prompt = scoring_prompt.format(job_description=job_description)
    
    try:
        response = get_gemini_response(job_description, pdf_content, formatted_prompt)
        # Extract scores from JSON at the end
        scores_start = response.rfind('{"Skills":')
        if scores_start != -1:
            scores_text = response[scores_start:].strip()
            scores = json.loads(scores_text)
        else:
            raise ValueError("No valid JSON scores found in response")
        
        # Validate scores
        for key in ["Skills", "Experience", "Keywords", "Formatting"]:
            if key not in scores or not isinstance(scores[key], (int, float)) or scores[key] < 0 or scores[key] > 100:
                raise ValueError(f"Invalid score for {key}")
        
        return {
            "Skills": int(scores["Skills"]),
            "Experience": int(scores["Experience"]),
            "Keywords": int(scores["Keywords"]),
            "Formatting": int(scores["Formatting"])
        }
    except Exception as e:
        print(f"Error in score_resume: {e}")
        return {"Skills": 50, "Experience": 50, "Keywords": 50, "Formatting": 50}