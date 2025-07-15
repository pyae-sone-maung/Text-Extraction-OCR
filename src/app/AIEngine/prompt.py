RESUME_EXTRACTION_PROMPT = """You are an HR data analyst. Extract employee data from resume into JSON. Include:
- name, email, phone, location
- social_links (list of URLs/usernames: e.g., LinkedIn, GitHub, Facebook, Viber, Telegram, etc)
- work_experience (list: title, company, dates, responsibilities)
- education (list: degree, institution, dates)
- skills (list: technical, soft_skills, communication_skills, other_skills)
- projects (list: name, description, technologies_used, project_url)
Resume Text: {resume_text}"""