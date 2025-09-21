import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os
from resume_analyzer import (
    extract_text_from_pdf, 
    extract_text_from_docx,
    extract_resume_highlights,
    rate_resume,
    generate_professional_summary,
    compare_with_job_title,
    format_analysis_output
)

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit App Configuration
st.set_page_config(page_title="Resume Analysis App", page_icon="📄", layout="wide")

st.title("📄 Resume Analysis App")
st.markdown("**Upload your resume and get instant analysis, rating, and improvement suggestions!**")

# Sidebar for file upload
with st.sidebar:
    st.header("📤 Upload Resume")
    uploaded_file = st.file_uploader("Choose your resume file", type=["pdf", "docx"])
    
    # Tips section
    st.markdown("---")
    st.markdown("### 💡 Pro Tips")
    st.info("""
    **For best results:**
    • Ensure your resume is well-formatted
    • Include clear sections for experience, skills, and education
    • Use readable fonts and proper spacing
    • Save as PDF for better text extraction
    """)
    
    if uploaded_file:
        st.success(f"✅ File uploaded: {uploaded_file.name}")

# Main content
if uploaded_file:
    # Extract text from uploaded file
    try:
        if uploaded_file.type == "application/pdf":
            resume_text = extract_text_from_pdf(uploaded_file)
        else:
            resume_text = extract_text_from_docx(uploaded_file)
    except Exception as e:
        st.error(f"❌ Error processing file: {str(e)}")
        resume_text = ""
    
    if resume_text.strip():
        # Create tabs for different analyses
        tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "⭐ Rating", "📝 Summary Generator", "🎯 Job Comparison"])
        
        with tab1:
            st.header("📊 Resume Highlights")
            
            with st.spinner("Extracting highlights..."):
                highlights = extract_resume_highlights(resume_text, model)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("🛠️ Skills")
                if highlights["skills"] and highlights["skills"][0] != "Unable to extract":
                    for skill in highlights["skills"][:10]:  # Limit to top 10
                        st.write(f"• {skill}")
                else:
                    st.write("No skills detected")
                
                st.subheader("🎓 Education")
                if highlights["education"] and highlights["education"][0] != "Unable to extract":
                    for edu in highlights["education"]:
                        st.write(f"• {edu}")
                else:
                    st.write("No education information detected")
            
            with col2:
                st.subheader("🚀 Projects")
                if highlights["projects"] and highlights["projects"][0] != "Unable to extract":
                    for project in highlights["projects"][:5]:  # Limit to top 5
                        st.write(f"• {project}")
                else:
                    st.write("No projects detected")
                
                st.subheader("📜 Certifications")
                if highlights["certifications"] and highlights["certifications"][0] != "Unable to extract":
                    for cert in highlights["certifications"]:
                        st.write(f"• {cert}")
                else:
                    st.write("No certifications detected")
            
            st.subheader("🔑 Key Information")
            col3, col4 = st.columns(2)
            with col3:
                st.metric("Experience", highlights["experience_years"])
            with col4:
                st.write("**Keywords:**")
                if highlights["keywords"] and highlights["keywords"][0] != "Unable to extract":
                    keywords_text = ", ".join(highlights["keywords"][:8])
                    st.write(keywords_text)
                else:
                    st.write("No keywords detected")
        
        with tab2:
            with st.spinner("Analyzing and rating your resume..."):
                rating_result = rate_resume(resume_text, model)
                # Format the output for better display
                formatted_rating = format_analysis_output(rating_result)
            
            st.markdown(formatted_rating)
        
        with tab3:
            st.header("📝 Professional Summary Generator")
            
            with st.spinner("Generating professional summary..."):
                summary = generate_professional_summary(resume_text, model)
            
            st.subheader("✨ Suggested Professional Summary")
            st.info(summary)
            
            st.subheader("📋 How to Use")
            st.markdown("""
            1. Copy the generated summary above
            2. Place it at the top of your resume, right after your contact information
            3. Customize it further if needed to match your personal style
            """)
        
        with tab4:
            st.header("🎯 Job Title Comparison")
            
            job_title = st.text_input("Enter target job title:", placeholder="e.g., Software Engineer, Data Scientist, Marketing Manager")
            
            if st.button("🔍 Analyze Match") and job_title:
                with st.spinner(f"Comparing your resume against '{job_title}' role..."):
                    comparison_result = compare_with_job_title(resume_text, job_title, model)
                    # Format the output for better display
                    formatted_comparison = format_analysis_output(comparison_result)
                
                st.markdown(formatted_comparison)
    
    else:
        st.error("❌ Could not extract text from the uploaded file. Please ensure it's a valid PDF or DOCX file with readable content.")

else:
    st.info("👆 Please upload your resume using the sidebar to get started!")
    
    # Show features when no file is uploaded
    st.markdown("## 🚀 What This App Offers:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📊 **Resume Highlights**
        - Extract skills, projects, and keywords
        - Identify education and certifications
        - Get key resume statistics
        
        ### ⭐ **Resume Rating**
        - Get rated out of 10 for clarity and impact
        - Understand your resume's strengths
        - Receive specific improvement suggestions
        """)
    
    with col2:
        st.markdown("""
        ### 📝 **Professional Summary**
        - Generate a compelling 2-line summary
        - Perfect for the top of your resume
        - Highlight key strengths effectively
        
        ### 🎯 **Job Comparison**
        - Compare against any job title
        - Identify missing skills
        - Get targeted recommendations
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <h3>🚀 Made by Adit Jain</h3>
    <p><em>Built with ❤️ for the Hack The Matrix hackathon</em></p>
    <p>Focused on solving real-world resume challenges for students and professionals</p>
</div>
""", unsafe_allow_html=True)