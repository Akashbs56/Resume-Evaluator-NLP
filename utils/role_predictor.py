import json

def get_role_skills(job_description, json_file="data/job_roles.json"):
    with open(json_file, "r", encoding="utf-8") as file:
        roles = json.load(file)

    jd = job_description.lower()

    for role, skills in roles.items():
        if role.lower() in jd:
            return skills

    return []