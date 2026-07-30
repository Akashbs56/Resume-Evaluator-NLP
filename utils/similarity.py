def calculate_similarity(resume_skills, jd_skills):
    resume_set = set(skill.lower() for skill in resume_skills)
    jd_set = set(skill.lower() for skill in jd_skills)

    if len(jd_set) == 0:
        return 0.0, set()

    matched = resume_set.intersection(jd_set)

    score = (len(matched) / len(jd_set)) * 100

    return round(score, 2), matched