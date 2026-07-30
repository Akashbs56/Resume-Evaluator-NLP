from utils.parser import extract_text
from utils.preprocess import preprocess_text
from utils.skill_extractor import extract_skills
from utils.similarity import calculate_similarity
from utils.ats_score import calculate_ats_score
from utils.suggestions import generate_suggestions

# -----------------------------------
# STEP 1: Read Resume
# -----------------------------------
resume_text = extract_text("resumes/sample_resume.pdf")
resume_text = preprocess_text(resume_text)
resume_skills = extract_skills(resume_text)

# -----------------------------------
# STEP 2: Read Job Description
# -----------------------------------
with open("data/sample_jd.txt", "r", encoding="utf-8") as file:
    jd_text = file.read()

jd_text = preprocess_text(jd_text)
jd_skills = extract_skills(jd_text)

# -----------------------------------
# STEP 3: Compare Resume & JD
# -----------------------------------
score, matched = calculate_similarity(resume_skills, jd_skills)

# -----------------------------------
# STEP 4: Calculate ATS Score
# -----------------------------------
rating, ats_score = calculate_ats_score(score)

# -----------------------------------
# STEP 5: Find Missing Skills
# -----------------------------------
missing_skills = generate_suggestions(resume_skills, jd_skills)

# -----------------------------------
# STEP 6: Display Results
# -----------------------------------

print("=" * 50)
print("        RESUME EVALUATOR REPORT")
print("=" * 50)

print("\nResume Skills:")
for skill in resume_skills:
    print("✓", skill)

print("\nJob Description Skills:")
for skill in jd_skills:
    print("✓", skill)

print("\nMatched Skills:")
for skill in matched:
    print("✓", skill)

print("\nMissing Skills:")
if missing_skills:
    for skill in missing_skills:
        print("✗", skill)
else:
    print("No missing skills.")

print("\n" + "=" * 50)
print(f"Resume Match Score : {score:.2f}%")
print(f"ATS Score          : {ats_score:.2f}%")
print(f"Rating             : {rating}")
print("=" * 50)