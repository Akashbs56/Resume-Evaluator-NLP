import pandas as pd
import re

def extract_skills(text, skills_file="data/skills.csv"):
    skills = pd.read_csv(skills_file, header=None)[0].tolist()

    found_skills = []

    text = text.lower()

    for skill in skills:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills