import streamlit as st
import tempfile
import os

from utils.parser import extract_text
from utils.preprocess import preprocess_text
from utils.skill_extractor import extract_skills
from utils.similarity import calculate_similarity
from utils.ats_score import calculate_ats_score
from utils.suggestions import generate_suggestions
from utils.role_predictor import get_role_skills
from utils.resume_sections import analyze_resume_sections

st.set_page_config(
    page_title="AI Resume Evaluator",
    page_icon="📄",
    layout="wide"
)

st.markdown("""
<style>

/* Main App Background */
.stApp{
    background: linear-gradient(135deg, #0F172A, #1E293B);
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background-color: #111827;
}

/* Metric Cards */
div[data-testid="stMetric"]{
    background: rgba(255,255,255,0.08);
    padding:20px;
    border-radius:15px;
    border:1px solid rgba(255,255,255,0.15);
    box-shadow:0 4px 20px rgba(0,0,0,0.3);
}

/* Buttons */
.stButton>button{
    background:#2563EB;
    color:white;
    border:none;
    border-radius:10px;
    padding:10px 20px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#1D4ED8;
}

/* Text Input */
textarea, input{
    background:#1E293B !important;
    color:white !important;
    border: 1px solid rgba(255,255,255,0.3) !important;
    border-radius: 8px !important;
}

textarea::placeholder{
    color: rgba(255,255,255,0.5) !important;
}

</style>
""", unsafe_allow_html=True)

st.title("🤖 AI Resume Evaluator & ATS Checker")
st.write("Upload your Resume and paste the Job Description.")

uploaded_resume = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf", "docx"]
)

job_description = st.text_area(
    "📝 Paste Job Description",
    height=250
)

if st.button("🚀 Analyze Resume"):

    if uploaded_resume is None:
        st.error("Please upload a resume.")
        st.stop()

    if job_description.strip() == "":
        st.error("Please enter the Job Description.")
        st.stop()

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=os.path.splitext(uploaded_resume.name)[1]
    ) as tmp:
        tmp.write(uploaded_resume.read())
        resume_path = tmp.name

    resume_text = extract_text(resume_path)
    resume_text = preprocess_text(resume_text)
    resume_skills = extract_skills(resume_text)

    jd_text = preprocess_text(job_description)

    jd_skills = get_role_skills(job_description)

    if not jd_skills:
        jd_skills = extract_skills(jd_text)

    score, matched = calculate_similarity(resume_skills, jd_skills)
    rating, ats_score = calculate_ats_score(score)
    missing_skills = generate_suggestions(resume_skills, jd_skills)

    sections = analyze_resume_sections(resume_text)

    st.success("✅ Analysis Completed Successfully!")

    st.header("📊 ATS Report")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("ATS Score", f"{score:.2f}%")
    with col2:
        st.metric("Rating", rating)

    st.progress(int(score))
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("✅ Resume Skills")
        if resume_skills:
            for skill in resume_skills:
                st.success(skill)
        else:
            st.warning("No skills found.")

        st.subheader("🟢 Matched Skills")
        if matched:
            for skill in matched:
                st.success(skill)
        else:
            st.warning("No matched skills found.")

    with col2:
        st.subheader("📌 Job Description Skills")
        if jd_skills:
            for skill in jd_skills:
                st.info(skill)
        else:
            st.error("No recognizable skills found.")

        st.subheader("❌ Missing Skills")
        if jd_skills == []:
            st.warning("Job Description contains no recognized technical skills.")
        elif missing_skills:
            for skill in missing_skills:
                st.error(skill)
        else:
            st.success("Excellent! No Missing Skills.")

    st.divider()

    st.header("📋 Resume Checklist")

    col1, col2 = st.columns(2)
    items = list(sections.items())

    with col1:
        for section, present in items[:3]:
            if present:
                st.success(f"✅ {section}")
            else:
                st.error(f"❌ {section}")

    with col2:
        for section, present in items[3:]:
            if present:
                st.success(f"✅ {section}")
            else:
                st.error(f"❌ {section}")

    st.divider()

    st.header("💡 AI Suggestions")
    if score >= 90:
        st.success("""
        🎉 Excellent Resume!
        ✔ ATS Friendly
        ✔ Strong Skill Match
        ✔ Ready to Apply
        """)
    elif score >= 75:
        st.info("""
Good Resume

Suggestions:

- Add more projects
- Add certifications
- Improve achievements
- Add GitHub & LinkedIn
""")
    elif score >= 50:
        st.warning("""
Average Resume

Improve by adding:

- Missing technical skills
- Better project descriptions
- Certifications
- Internship experience
- Portfolio
""")
    else:
        st.error("""
Needs Improvement

Suggestions:

- Add required skills
- Add projects
- Add certifications
- Customize resume for each job
- Improve resume formatting
""")

    os.remove(resume_path)