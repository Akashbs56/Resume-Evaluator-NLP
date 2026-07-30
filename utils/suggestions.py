def generate_suggestions(resume_skills, jd_skills):
    """
    Generate suggestions based on missing skills.
    """

    resume_set = set(skill.lower() for skill in resume_skills)
    jd_set = set(skill.lower() for skill in jd_skills)

    missing = jd_set - resume_set

    return list(missing)