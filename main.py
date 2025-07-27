import streamlit as st
import json
import re
from utils import input_pdf_setup, get_gemini_response, score_resume
from prompts import input_prompt1, input_prompt2, input_prompt3, input_prompt4

# Set up page configuration
st.set_page_config(
    page_title="ATS Resume Checker",
    page_icon="📄",
    layout="wide"
)

# Load external CSS
st.markdown('<link rel="stylesheet" href="style.css">', unsafe_allow_html=True)

# Initialize session state for inputs
if 'job_requirements' not in st.session_state:
    st.session_state.job_requirements = ""
if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None
if 'pdf_content' not in st.session_state:
    st.session_state.pdf_content = None

# Main content
st.markdown('<h1 class="main-title">📄 ATS Resume Checker</h1>', unsafe_allow_html=True)

# Input section
with st.container():
    st.markdown('<h2 class="subheader">Input Details</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1], gap="medium")

    with col1:
        job_requirements = st.text_area(
            "💼 Job Description",
            value=st.session_state.job_requirements,
            placeholder="Paste the job description here...",
            height=250,
            help="Enter the job description to compare against your resume.",
            key="job_description_input"
        )
        # Update session state
        st.session_state.job_requirements = job_requirements

    with col2:
        uploaded_file = st.file_uploader(
            "📁 Upload Resume",
            type=["pdf"],
            help="Upload your resume in PDF format.",
            key="file_uploader"
        )
        # Process file only if new upload
        if uploaded_file != st.session_state.uploaded_file:
            st.session_state.uploaded_file = uploaded_file
            if uploaded_file:
                st.session_state.pdf_content = input_pdf_setup(uploaded_file)

# Analysis buttons
st.markdown("---")
st.markdown('<h2 class="subheader">Choose Analysis Type</h2>', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4, gap="small")

with col1:
    submit1 = st.button("📊 Resume Breakdown", use_container_width=True)
with col2:
    submit2 = st.button("💼 Job Recommendations", use_container_width=True)
with col3:
    submit3 = st.button("📝 Interview Tips", use_container_width=True)
with col4:
    submit4 = st.button("📋 ATS Match Analysis", use_container_width=True)

# Function to display AI response and score breakdown
def display_response(prompt, category_name):
    if st.session_state.uploaded_file is not None and st.session_state.pdf_content is not None:
        with st.spinner("Analyzing your resume..."):
            # Combine scoring and detailed analysis in one API call
            combined_prompt = f"""
            {prompt}
            Tailor the response specifically to the {category_name} category. Ensure the response is unique to this category and avoids overlap with other analysis types (e.g., Resume Breakdown, Job Recommendations, Interview Tips, ATS Match Analysis).

            Follow with a detailed breakdown of each score category, explaining the evaluation:
            - Skills: Describe the match of technical/soft skills to job requirements.
            - Experience: Evaluate relevance and duration of work experience.
            - Keywords: Assess presence of key terms from the job description.
            - Formatting: Analyze ATS-friendliness and readability.

            At the end, "🛠️Skills": X%,
              "💼Experience": Y%,
                "🔑Keywords": Z%,
                  "📋 Formatting": W% print each of these in new line 
            """
            response = get_gemini_response(st.session_state.job_requirements, st.session_state.pdf_content, combined_prompt)
            
            # Extract scores from response
            try:
                scores_start = response.rfind('{"Skills":')
                if scores_start != -1:
                    scores_text = response[scores_start:].strip()
                    scores = json.loads(scores_text)
                    # Remove JSON from response
                    response = response[:scores_start].strip()
                else:
                    scores = score_resume(st.session_state.job_requirements, st.session_state.pdf_content)
                
                # Validate scores
                for key in ["Skills", "Experience", "Keywords", "Formatting"]:
                    if key not in scores or not isinstance(scores[key], (int, float)) or scores[key] < 0 or scores[key] > 100:
                        raise ValueError(f"Invalid score for {key}")
                scores = {k: int(v) for k, v in scores.items()}
            except Exception as e:
                print(f"Error parsing scores: {e}")
                scores = score_resume(st.session_state.job_requirements, st.session_state.pdf_content)
            
            # Display score breakdown with each category on a new line
            st.markdown('<h3 class="subheader">Resume Score Breakdown</h3>', unsafe_allow_html=True)
            st.markdown(f'<h4 class="subheader"><span class="score-skills">🛠️ <strong>{scores["Skills"]}% SKILLS</strong></span></h4>', unsafe_allow_html=True)
            st.markdown(f'<h4 class="subheader"><span class="score-experience">💼 <strong>{scores["Experience"]}% EXPERIENCE</strong></span></h4>', unsafe_allow_html=True)
            st.markdown(f'<h4 class="subheader"><span class="score-keywords">🔑 <strong>{scores["Keywords"]}% KEYWORDS</strong></span></h4>', unsafe_allow_html=True)
            st.markdown(f'<h4 class="subheader"><span class="score-formatting">📋 <strong>{scores["Formatting"]}% FORMATTING</strong></span></h4>', unsafe_allow_html=True)
            
            # Display detailed response (including breakdown and feedback)
            st.markdown('<h2 class="subheader">Detailed Feedback</h2>', unsafe_allow_html=True)
            st.markdown(response)
    else:
        st.warning("Please upload a resume file before proceeding.", icon="⚠️")

# Handle button clicks
if submit1:
    display_response(input_prompt1, "Resume Breakdown")
elif submit2:
    display_response(input_prompt2, "Job Recommendations")
elif submit3:
    display_response(input_prompt3, "Interview Tips")
elif submit4:
    display_response(input_prompt4, "ATS Match Analysis")