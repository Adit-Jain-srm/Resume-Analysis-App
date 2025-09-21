# 📄 Resume Analysis App - GenAI-Powered Solutions

**An AI-powered resume analyzer that helps students and professionals create impactful resumes that stand out to recruiters.**

Built for the **Hack The Matrix** hackathon, this intelligent resume analysis tool leverages **Google Gemini AI** to provide comprehensive resume insights, ratings, and improvement suggestions.

---

## 🎯 Problem Statement

Resumes are critical for job applications, yet most fail to create strong impact due to:
- ❌ Unclear formatting and weak wording
- ❌ Missing relevant keywords and skills  
- ❌ Lack of action-oriented project descriptions
- ❌ Poor professional tone and clarity
- ❌ Ineffective professional summaries

**Recruiters spend only seconds scanning resumes** - making it essential to highlight key skills, projects, and experiences effectively.

---

## ✨ Solution Features

Our **Resume Analysis App** provides instant analysis when you upload your resume (PDF/DOCX):

### 📊 **Resume Highlights Extraction**
- 🛠️ **Skills**: Technical and professional skills identification
- 🚀 **Projects**: Key projects and descriptions
- 🔑 **Keywords**: Important buzzwords and terms
- 🎓 **Education & Certifications**: Academic background analysis

### ⭐ **Resume Rating System**
- 📈 **Score out of 10** for clarity and impact
- 💪 **Strengths identification** - what's working well
- 🔧 **Improvement suggestions** - specific areas to enhance

### 📝 **Professional Summary Generator**
- ✨ **2-line compelling summary** for resume top
- 🎯 **Attention-grabbing** content that highlights key strengths
- 📋 **Ready-to-use** format for immediate implementation

### 🎯 **Job Title Comparison**
- 🔍 **Match percentage** against target roles
- 🚫 **Missing skills identification** for specific positions
- 💡 **Targeted recommendations** to improve job fit

---

## 🚀 Tech Stack

- **Python 3.10+**
- **Streamlit** - Interactive web interface
- **Google Gemini AI** - Advanced language model for analysis
- **PyPDF2** - PDF text extraction
- **python-docx** - DOCX file processing

---

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd Resume-Analysis-App
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Google AI API Key
Create a `.env` file in the root directory:
```env
GOOGLE_API_KEY="your_gemini_api_key_here"
```

🔑 Get your API key at [Google AI Studio](https://aistudio.google.com/app/apikey)

### 4. Run the Application
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 💻 How to Use

1. **📤 Upload Resume**: Use the sidebar to upload your PDF or DOCX resume
2. **📊 View Highlights**: See extracted skills, projects, and keywords
3. **⭐ Check Rating**: Get your resume rated out of 10 with detailed feedback
4. **📝 Generate Summary**: Create a professional 2-line summary for your resume
5. **🎯 Compare Jobs**: Enter target job titles to identify skill gaps

---

## 🎪 Hackathon Submission

This project was built for the **GenAI-Powered Solutions: Hack The Matrix** hackathon, addressing the critical need for better resume optimization tools for students and professionals.

### Key Hackathon Requirements Met:
- ✅ Resume upload and text extraction (PDF support)
- ✅ Highlights extraction (skills, projects, keywords)
- ✅ Resume rating system (out of 10)
- ✅ Improvement suggestions for each section
- ✅ Professional summary generation (2-line format)
- ✅ Job title comparison with missing skills identification

---

## 🔧 Technical Implementation

### Core Functions:
- `extract_resume_highlights()` - AI-powered skill and project extraction
- `rate_resume()` - Comprehensive resume scoring system
- `generate_professional_summary()` - Compelling summary creation
- `compare_with_job_title()` - Job-specific gap analysis

### AI Prompting Strategy:
- Structured prompts for consistent JSON output
- Context-aware analysis for personalized feedback
- Multi-criteria evaluation for comprehensive ratings

---

## 🌟 Future Enhancements

- 📊 **Resume Templates**: AI-suggested formatting improvements
- 🔄 **Before/After Comparison**: Visual resume improvement tracking
- 📈 **Industry-Specific Analysis**: Tailored insights by field
- 🎨 **Visual Resume Builder**: Integrated design tools

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 📸 Screenshots

### Main Interface
<img width="1839" height="794" alt="image" src="https://github.com/user-attachments/assets/f1361ffd-2bb6-4b40-8314-9ea35070022c" />
*Clean and intuitive interface for uploading resumes*

### Resume Rating & Feedback
<img width="1827" height="811" alt="image" src="https://github.com/user-attachments/assets/761b18e3-dc5d-4d00-851a-a6ca3fd18032" />
<img width="1802" height="813" alt="image" src="https://github.com/user-attachments/assets/aa1908c9-70e6-4d84-b100-50ab90cd3455" />
*Detailed rating with strengths and improvement areas*

### Job Comparison Analysis
<img width="1785" height="789" alt="image" src="https://github.com/user-attachments/assets/d47839a6-1d43-46a4-8de0-4adfbe83774c" />
<img width="1796" height="809" alt="image" src="https://github.com/user-attachments/assets/b610f1a9-a902-4e39-8cbe-d70cddb6f00b" />

*Smart comparison against target job roles*

---

## 🎓 Learning Outcomes

Through this project, I gained valuable experience in:
- **AI Integration**: Successfully integrated Google Gemini API for intelligent resume analysis and natural language processing
- **Problem Identification & Solution**: Identified real-world resume challenges and built a comprehensive solution that addresses formatting, content gaps, and job alignment issues

---

## 👥 Creator

<div align="center">

**Made by Adit Jain** 🚀

*Built with ❤️ for the Hack The Matrix hackathon*

*Focused on solving real-world resume challenges for students and professionals*

</div>

---

**🚀 Ready to transform your resume? Upload it now and get instant AI-powered insights!**
