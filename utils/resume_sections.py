import re

def analyze_resume_sections(text):
    text = text.lower()

    sections = {
        "Education": bool(re.search(r"education|b\.?e|btech|degree|college|university", text)),
        "Projects": bool(re.search(r"project|projects", text)),
        "Experience": bool(re.search(r"experience|work experience|internship", text)),
        "Certifications": bool(re.search(r"certification|certifications|certificate", text)),
        "Skills": bool(re.search(r"skills|technical skills", text))
    }

    return sections