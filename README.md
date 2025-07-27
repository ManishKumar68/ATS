This is a ATS project.
Job Portal App with AI Resume Scanner

 ----------------------------------------------------------------------------------------------------------------------------------------
StudyMaterial: Job Portal App with AI Resume Scanner
 
 ProjectTeam  May22,2025 Document Overview
 
 Version: 1.0
 
 Preparedfor: StudentsandDevelopers
 
 Contents
 1 Introduction . . . . . . . . . . . . . . . . . 
 
 1.1 Objectives . . . . . . . . . . . . . . . .  
 
 1.2 Purpose . . . . . . . . . . . . . . . . .  
 
 2 TechnologiesUsed. . . . . . . . . . . . . . 
 
 2.1 MERNStack. . . . . . . . . . . . . . . . 
 
 2.2 AdditionalTools . . . . . . . . . . . .
 
 3 SystemArchitecture . . . . . . . . . . . . 
 
 3.1 PresentationLayer . . . . . . . . . . . . 
 
 3.2 BusinessLogicLayer . . . . . . . . . . . 
 
 3.3 DataAccessLayer. . . . . . . . . . . . . 
 
 4 AIResumeScanner . . . . . . . . . . . . . 
 
 4.1 Functionality. . . . . . . . . . . . . . 
 
 4.2 Implementation . . . . . . . . . . . . . .
 
 5 DevelopmentProcess . . . . . . . . . . . . 
 
 5.1 TeamRoles . . . . . . . . . . . . . . . .
 
 5.2 Phases . . . . . . . . . . . . . . . . . . .
 
 6 KeyFeatures . . . . . . . . . . . . . . . . .
 
 7 LearningOutcomes . . . . . . . . . . . . . 

 
 1 Introduction
 
The Job Portal App with AIResumeScanner isafull-stack web application design edtostreamlinerecruitment
 byconnectingjobseekersandemployers.BuiltusingtheMERNstack(MongoDB,Express.js,React.js,Node.js),
 itoffersfeatureslikejobposting,applicationtracking,andanAI-poweredresumescannerthatmatchesresumes
 to jobrequirementsusingnatural languageprocessing(NLP).Theapplicationensures secureauthentication,
 responsivedesign,andcloud-basedscalability.
 
 1.1Objectives
 •Simplifyjobsearchingandhiringwithanintuitiveplatform.
 •ReducemanualresumescreeningusingAI-drivenanalysis.
 •Providesecure,responsive,andscalableservicesforusers.
 
 1.2Purpose
 This studymaterial introduces students to full-stackdevelopment, AI integration, andmodern recruitment
 systems,usingtheJobPortalAppasapracticalexample.
 [InsertProjectWorkflowPlaceholder]
 Figure1:ProjectWorkflowDiagram
 2TechnologiesUsed
 Theprojectleveragesmoderntoolsandframeworkstodeliverarobustapplication.
 
 1
2.1 MERN Stack
 • MongoDB: NoSQL database for flexible storage of job listings, user profiles, and applications.
 • Express.js: Backend framework for RESTful APIs and routing.
 • React.js: Frontend library for dynamic, responsive UI with Bootstrap for styling.
 • Node.js: Server-side runtime for scalable API handling.
 
 2.2 Additional Tools
 • Cloudinary: Cloud storage for profile images and resumes.
 • JWT&Bcrypt: Secure authentication and password hashing.
 • NLP Libraries: Used for AI resume parsing (e.g., similar to ‘utils.py‘ in ATS Resume Checker for PDF
 processing).
 • Deployment: Vercel (frontend), Render (backend), MongoDB Atlas (database).
 
 3 System Architecture
 The application follows a 3-tier architecture for modularity and scalability.
 
 3.1 Presentation Layer
 • Built with React.js and Bootstrap.
 • Handles user interactions (e.g., job browsing, resume uploads).
 • Responsive across desktops, tablets, and smartphones.
 
 3.2 Business Logic Layer
 • Powered by Node.js and Express.js.
 • Manages authentication (JWT), AI resume scanning, and API logic.
 • Example: Similar to ‘main.py‘’s ‘displayresponse‘functionforprocessingAIresponses.
 
 3.3 Data Access Layer
 • Uses MongoDB Atlas for storing user data, jobs, and applications.
 • Communicates via Mongoose schemas, ensuring data integrity.
 [Insert Architecture Diagram Placeholder]
 Figure 2: 3-Tier Architecture
 
 4 AI Resume Scanner
 The AI resume scanner is a core feature, using NLP to parse resumes and match them to job descriptions.
 
 4.1 Functionality
 • Parsing: Extractsskills, experience, and keywords from resumes (similar to ‘utils.py‘’s ‘inputpdfsetup‘forPDFprocessing
 Scoresresumesbasedonjobrequirements(e.g.,skills,keywords).
 • Output: Provides match scores and highlights relevant qualifications.
 
 4.2 Implementation
 • UsesNLPlibraries to analyze text, akin to ‘scoreresume‘in‘utils.py‘.Integratedintothebackend,triggeredwhenemployersviewapplications.
 2
 
5 Development Process
 The project was developed using the Incremental Rapid Application Development (RAD) model over 20 days.
 
 5.1 Team Roles
 • Frontend Developer: Built UI with React.js and Bootstrap.
 • Backend Developer: Created APIs with Node.js and Express.js.
 • AI Developer: Implemented NLP for resume scanning.
 • DevOps: Managed deployment on Vercel, Render, and MongoDB Atlas.
 
 5.2 Phases
 • Planning: 2 days for requirement gathering.
 • Design: 3 days for UI/UX and database schema.
 • Development: 8 days for coding and unit testing.
 • Integration: 3 days for bug fixing and testing.
 • Deployment: 2 days for cloud setup.
 
 6 Key Features
 • Job Seekers: Register, upload resumes, apply for jobs, track applications.
 • Employers: Post jobs, view applications, use AI scanner for candidate selection.
 • Authentication: Secure login with JWT and Bcrypt.
 • Reports: Application status, job posting summaries, AI match scores.
 • Responsiveness: Accessible on all devices via Bootstrap.
 [Insert UI Screenshot Placeholder]
 
 Figure 3: Sample UI Screenshot
 
 7 Learning Outcomes
 Students studying this project will gain:
 • Full-Stack Development: Hands-on experience with MERN stack.
 • AI Integration: Understanding NLP for resume parsing, as seen in ‘prompts.py‘ for ATS analysis.
 • Security: Implementing JWT and Bcrypt for secure authentication.
 • Deployment: Using cloud platforms like Vercel and MongoDB Atlas.
 • Team Collaboration: Managing roles in a development project.


 Project Runing Step-by-step
 step 1 - python -m venv venv
 step 2 - ./venv\Scripts\activate
 step 3 - pip install requirements.txt
 step 4 - streamlit run main.py 
