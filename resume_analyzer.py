"""
Resume Analysis Utilities
Contains all the core functions for resume analysis and processing.
"""

import json
import google.generativeai as genai

def extract_text_from_pdf(uploaded_file):
    """Extract text from PDF file"""
    import PyPDF2
    reader = PyPDF2.PdfReader(uploaded_file)
    return "\n".join([page.extract_text() for page in reader.pages])

def extract_text_from_docx(uploaded_file):
    """Extract text from DOCX file"""
    import docx
    doc = docx.Document(uploaded_file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_resume_highlights(resume_text, model):
    """Extract skills, projects, and keywords from resume"""
    prompt = f"""
    Analyze the following resume and extract key information in JSON format:
    
    Resume Text:
    {resume_text}
    
    Extract and return ONLY a valid JSON object with these keys:
    {{
        "skills": ["list of technical and professional skills"],
        "projects": ["list of project names and brief descriptions"],
        "keywords": ["important keywords and buzzwords"],
        "experience_years": "estimated years of experience",
        "education": ["educational qualifications"],
        "certifications": ["any certifications mentioned"]
    }}
    
    Make sure to return only the JSON object, no additional text.
    """
    
    try:
        response = model.generate_content(prompt)
        # Clean the response to extract JSON
        response_text = response.text.strip()
        if response_text.startswith('```json'):
            response_text = response_text[7:-3]
        elif response_text.startswith('```'):
            response_text = response_text[3:-3]
        
        return json.loads(response_text)
    except:
        # Fallback if JSON parsing fails
        return {
            "skills": ["Unable to extract"],
            "projects": ["Unable to extract"],
            "keywords": ["Unable to extract"],
            "experience_years": "Unknown",
            "education": ["Unable to extract"],
            "certifications": ["Unable to extract"]
        }

def rate_resume(resume_text, model):
    """Rate resume out of 10 for clarity and impact"""
    prompt = f"""
    Rate this resume out of 10 based on clarity, impact, and professional presentation. 
    Consider factors like:
    - Clear formatting and structure
    - Strong action-oriented descriptions
    - Relevant skills and experience
    - Professional tone
    - Quantified achievements
    
    Resume:
    {resume_text}
    
    Format your response with proper line breaks and structure:
    
    ## ⭐ Resume Rating
    **X/10** - Brief one-line summary of overall quality
    
    ## 📝 Analysis
    Write 2-3 sentences explaining the rating, highlighting what works well and what needs improvement.
    
    ## 💪 Top Strengths
    • **Strength 1**: Brief explanation
    • **Strength 2**: Brief explanation  
    • **Strength 3**: Brief explanation
    
    ## 🔧 Areas for Improvement
    • **Improvement 1**: Specific actionable suggestion
    • **Improvement 2**: Specific actionable suggestion
    • **Improvement 3**: Specific actionable suggestion
    
    Keep each point concise and actionable. Use proper line breaks between sections.
    """
    
    response = model.generate_content(prompt)
    return response.text

def generate_professional_summary(resume_text, model):
    """Generate a 2-line professional summary"""
    prompt = f"""
    Based on this resume, create a compelling 2-line professional summary that could be placed at the top of the resume.
    The summary should:
    - Highlight key strengths and experience
    - Be concise and impactful
    - Use strong action words
    - Be exactly 2 lines/sentences
    
    Resume:
    {resume_text}
    
    Return only the 2-line summary, nothing else.
    """
    
    response = model.generate_content(prompt)
    return response.text.strip()

def compare_with_job_title(resume_text, job_title, model):
    """Compare resume against target job title with proper formatting"""
    prompt = f"""
    Compare this resume against the target job title: "{job_title}"
    
    Resume:
    {resume_text}
    
    Analyze and provide a structured response with proper line breaks and formatting.
    
    Format your response EXACTLY like this with proper spacing:
    
    ## 🎯 Match Score
    **X%** - Brief reason for this score
    
    ## 🚫 Missing Skills
    • **Skill 1**: Brief explanation of why this skill is important
    • **Skill 2**: Brief explanation of why this skill is important  
    • **Skill 3**: Brief explanation of why this skill is important
    • **Additional skills**: If needed
    
    ## 📊 Experience Alignment
    Write a clear paragraph analyzing how the current experience aligns with the target role. Keep it concise but informative.
    
    ## 💡 Recommendations
    • **Action 1**: Specific recommendation with clear next steps
    • **Action 2**: Specific recommendation with clear next steps
    • **Action 3**: Specific recommendation with clear next steps
    • **Additional recommendations**: If needed
    
    IMPORTANT: 
    - Keep bullet points concise (1-2 lines each)
    - Use proper line breaks between sections
    - Make recommendations actionable and specific
    - Ensure proper markdown formatting
    """
    
    response = model.generate_content(prompt)
    return response.text

def format_analysis_output(text):
    """Clean and format analysis output to ensure proper line breaks"""
    # Ensure proper spacing between sections
    text = text.replace('## ', '\n## ')
    text = text.replace('• **', '\n• **')
    
    # Clean up multiple newlines
    while '\n\n\n' in text:
        text = text.replace('\n\n\n', '\n\n')
    
    # Ensure sections start on new lines
    sections = ['🎯 Match Score', '🚫 Missing Skills', '📊 Experience Alignment', '💡 Recommendations',
                '⭐ Resume Rating', '📝 Analysis', '💪 Top Strengths', '🔧 Areas for Improvement']
    
    for section in sections:
        text = text.replace(f'## {section}', f'\n## {section}')
    
    return text.strip()
