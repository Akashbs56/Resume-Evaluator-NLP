# 🤖 AI Resume Evaluator & ATS Checker using NLP

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red)
![NLP](https://img.shields.io/badge/NLP-Powered-orange)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Open Source](https://img.shields.io/badge/Open%20Source-Yes-success)

An AI-powered Resume Evaluation System built using **Python**, **Natural Language Processing (NLP)**, and **Streamlit**. The application analyzes resumes, extracts technical skills, predicts job roles, compares resumes with job descriptions, calculates ATS scores, identifies missing skills, and provides intelligent suggestions to improve resume quality and job readiness.

---

# 📑 Table of Contents

- About
- Features
- Project Architecture
- Technologies Used
- Project Structure
- Installation
- Usage
- Working Principle
- System Modules
- Dataset
- Libraries Used
- ATS Score Calculation
- Performance
- Testing
- Applications
- Roadmap
- Future Enhancements
- FAQ
- Troubleshooting
- Contributing
- Security
- License
- Acknowledgements
- Author
- Support

---

# 📖 About

Recruiters often receive hundreds of resumes for a single job opening. Most companies use **Applicant Tracking Systems (ATS)** to automatically filter resumes before a recruiter reviews them.

The **AI Resume Evaluator & ATS Checker** helps candidates optimize their resumes by comparing them with job descriptions and providing actionable feedback.

The project uses Natural Language Processing (NLP) techniques to analyze resume content, identify important skills, calculate ATS compatibility, detect missing resume sections, and recommend improvements.

---

# ✨ Features

- 📄 Upload PDF and DOCX resumes
- 📑 Automatic resume parsing
- 🧠 NLP-based text preprocessing
- 🎯 ATS Score Calculation
- 🤖 AI Job Role Prediction
- 📊 Resume vs Job Description Matching
- 🔍 Skill Extraction
- 📈 Skill Gap Analysis
- 📋 Resume Section Detection
- 💡 Resume Improvement Suggestions
- ✅ Resume Checklist
- 📉 Missing Skills Identification
- 📌 Matched Skills Detection
- 📚 Job-Specific Skill Recommendations
- 🏆 Recruiter Style Resume Evaluation
- 📊 Interactive Dashboard
- 🌙 Modern Streamlit UI
- ⚡ Fast Resume Processing
- 🔒 Secure Local Processing
- 💻 Cross Platform Support
- 📂 Beginner Friendly Project
- 🧩 Modular Python Code
- 📈 Data Visualization Support
- 🚀 Open Source
- 🔄 Easy to Extend
- 📥 Future PDF Report Generation
- 🤝 Community Contributions Welcome

---

# 🏗️ Project Architecture

```
Resume Upload
      │
      ▼
Resume Parser
      │
      ▼
Text Preprocessing
      │
      ▼
Skill Extraction
      │
      ▼
Job Role Prediction
      │
      ▼
Resume & JD Comparison
      │
      ▼
ATS Score Calculation
      │
      ▼
Suggestions Generation
      │
      ▼
Interactive Dashboard
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Streamlit | Web Application |
| NLP | Text Processing |
| Pandas | Data Processing |
| PDFPlumber | PDF Parsing |
| python-docx | DOCX Parsing |
| Scikit-learn | Machine Learning |
| JSON | Job Role Database |
| Regex | Text Cleaning |

---

# 📂 Project Structure

```
Resume-Evaluator-NLP
│
├── app.py
├── requirements.txt
├── README.md
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE
├── data
│   ├── skills.csv
│   ├── sample_jd.txt
│   └── job_roles.json
├── resumes
│   └── sample_resume.pdf
└── utils
    ├── parser.py
    ├── preprocess.py
    ├── skill_extractor.py
    ├── similarity.py
    ├── ats_score.py
    ├── role_predictor.py
    ├── suggestions.py
    └── resume_sections.py
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/Resume-Evaluator-NLP.git
```

Navigate to the project

```bash
cd Resume-Evaluator-NLP
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 🚀 Usage

1. Launch the application.
2. Upload a resume (PDF or DOCX).
3. Enter a Job Description.
4. Click **Analyze Resume**.
5. View the ATS Score.
6. Review matched and missing skills.
7. Check resume sections.
8. Follow AI-generated suggestions.

---

# ⚙️ Working Principle

1. Resume Upload
2. Resume Parsing
3. Text Preprocessing
4. Skill Extraction
5. Job Role Prediction
6. Resume and Job Description Comparison
7. ATS Score Calculation
8. Resume Section Detection
9. Missing Skill Analysis
10. AI Suggestions
11. Dashboard Visualization

---

# 📦 System Modules

### Resume Parser
Extracts text from PDF and DOCX resumes.

### Text Preprocessing
Removes unwanted symbols and normalizes text.

### Skill Extraction
Identifies technical skills using predefined datasets.

### Similarity Module
Compares resume skills with job description skills.

### ATS Score Calculator
Calculates compatibility score based on matching skills.

### Job Role Predictor
Predicts suitable job roles using keyword matching.

### Resume Section Analyzer
Checks for Education, Skills, Projects, Experience, and Certifications.

### Suggestion Generator
Recommends missing skills and improvements.

### Streamlit Dashboard
Displays ATS score, skill analysis, and recommendations.

---

# 📊 Dataset

The project includes:

- skills.csv
- job_roles.json
- sample_resume.pdf
- sample_jd.txt

---

# 📚 Libraries Used

- Streamlit
- Pandas
- PDFPlumber
- python-docx
- Scikit-learn
- NumPy
- JSON
- Regular Expressions (re)

---

# 📈 ATS Score Calculation

The ATS score is calculated using:

```
Matched Skills
────────────── × 100
Required Skills
```

### Example

Required Skills

- Python
- SQL
- Tableau
- Excel

Resume Skills

- Python
- SQL

ATS Score

```
2 / 4 × 100 = 50%
```

---

# ⚡ Performance

- Lightweight architecture
- Fast resume parsing
- Efficient NLP preprocessing
- Accurate skill extraction
- Responsive dashboard
- Local processing for better privacy

---

# 🧪 Testing

The application has been tested for:

- PDF Upload
- DOCX Upload
- ATS Calculation
- Skill Matching
- Resume Parsing
- Dashboard Rendering
- Error Handling
- UI Responsiveness

---

# 📌 Applications

- Resume Screening
- College Placement Preparation
- Recruitment Automation
- Career Guidance
- Resume Optimization
- Skill Gap Analysis
- HR Recruitment
- Job Matching

---

# 🗺️ Roadmap

- ✅ Resume Parsing
- ✅ ATS Score
- ✅ Skill Extraction
- ✅ Job Role Prediction
- ✅ Resume Checklist
- ⬜ Resume Builder
- ⬜ AI Resume Writer
- ⬜ PDF Report Export
- ⬜ AI Interview Questions
- ⬜ Resume Ranking
- ⬜ LinkedIn Profile Analysis
- ⬜ Multi-language Support

---

# 🚀 Future Enhancements

- AI Resume Builder
- AI Chat Assistant
- Resume Ranking System
- Interview Preparation Module
- Resume PDF Export
- LinkedIn Integration
- Company Specific ATS
- Resume History Tracking
- Cloud Database Integration
- User Authentication
- Email Report Generation
- AI Grammar Checker
- Mobile Responsive Dashboard

---

# ❓ FAQ

### Does it support DOCX files?

Yes.

### Does it support PDF resumes?

Yes.

### Does it store uploaded resumes?

No. Resume processing is performed locally.

### Can I upload multiple resumes?

Currently, one resume can be analyzed at a time.

---

# 🛠️ Troubleshooting

**ModuleNotFoundError**

Install dependencies:

```bash
pip install -r requirements.txt
```

**Streamlit Not Found**

```bash
pip install streamlit
```

**PDF Not Reading**

Ensure the PDF contains selectable text and is not a scanned image.

---

# 🤝 Contributing

Contributions are always welcome.

You can contribute by:

- Fixing bugs
- Improving ATS algorithms
- Enhancing NLP modules
- Improving UI/UX
- Writing documentation
- Adding new features
- Optimizing performance
- Improving testing

Please read **CONTRIBUTING.md** before submitting a Pull Request.

---

# 🔒 Security

Please review **SECURITY.md** for information on reporting vulnerabilities and following responsible disclosure practices.

---

# 📜 License

This project is licensed under the **MIT License**.

See the LICENSE file for more information.

---

# 🙏 Acknowledgements

Special thanks to:

- Python Community
- Streamlit
- Scikit-learn
- PDFPlumber
- Open Source Contributors
- GitHub Community

---

# 👨‍💻 Author

**Akash B S**

Information Science & Engineering Student

Skills:

- Python
- Java
- NLP
- Machine Learning
- Streamlit
- Full Stack Development

GitHub: https://github.com/your-username

LinkedIn: https://linkedin.com/in/your-profile

---

# ⭐ Support

If you found this project useful:

- ⭐ Star this repository
- 🍴 Fork the repository
- 🐞 Report bugs
- 💡 Suggest new features
- 🤝 Contribute to the project

Your support motivates future improvements and helps others discover this project.

---

## ❤️ Thank You

Thank you for visiting **AI Resume Evaluator & ATS Checker using NLP**.

Happy Coding! 🚀
