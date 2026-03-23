import streamlit as st

# ── Page config ──────────────────────────────────────────────
st.set_page_config(
    page_title="Job Recommendation System",
    page_icon="🎯",
    layout="wide"
)

# ── Custom CSS ───────────────────────────────────────────────
st.markdown("""
<style>
.main-header {
    background: linear-gradient(135deg, #16213e, #0f3460);
    padding: 40px; border-radius: 12px;
    text-align: center; color: white; margin-bottom: 32px;
}
.main-header h1 { font-size: 2.5rem; margin-bottom: 8px; }
.main-header h1 span { color: #e94560; }
.main-header p { color: #b0c4de; font-size: 1.1rem; }

.job-card {
    background: white; border-left: 4px solid #e94560;
    border-radius: 8px; padding: 20px; margin-bottom: 16px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
}
.match-badge {
    background: #e94560; color: white;
    padding: 4px 12px; border-radius: 20px;
    font-size: 0.85rem; font-weight: bold; float: right;
}
.step-card {
    background: #f8f9fa; border-radius: 10px;
    padding: 20px; margin-bottom: 16px;
    border-left: 4px solid #0f3460;
}
.skill-have {
    background: #e6f9ec; color: #28a745;
    padding: 4px 12px; border-radius: 20px;
    display: inline-block; margin: 4px;
    font-size: 0.85rem; font-weight: 600;
}
.skill-missing {
    background: #fde8ec; color: #e94560;
    padding: 4px 12px; border-radius: 20px;
    display: inline-block; margin: 4px;
    font-size: 0.85rem; font-weight: 600;
}
</style>
""", unsafe_allow_html=True)


# ── Job Knowledge Base ────────────────────────────────────────
JOB_KB = [
    {
        "title": "AI Engineer",
        "company_type": "Tech / Product",
        "salary": "₹12–25 LPA",
        "required_skills": ["Python", "TensorFlow", "PyTorch",
                            "Machine Learning", "Docker", "AWS"],
        "description": "Design, build, and deploy AI/ML models into production systems."
    },
    {
        "title": "Data Scientist",
        "company_type": "Analytics / Consulting",
        "salary": "₹8–18 LPA",
        "required_skills": ["Python", "R", "SQL", "Statistics", "Pandas", "Tableau"],
        "description": "Analyse large datasets to extract insights and build predictive models."
    },
    {
        "title": "Machine Learning Engineer",
        "company_type": "Startup / Enterprise",
        "salary": "₹10–20 LPA",
        "required_skills": ["Python", "scikit-learn", "Spark", "SQL", "Docker"],
        "description": "Build and maintain ML pipelines and model training infrastructure."
    },
    {
        "title": "Full Stack Developer",
        "company_type": "Product / Service",
        "salary": "₹6–16 LPA",
        "required_skills": ["HTML", "CSS", "JavaScript", "Node.js", "React", "MySQL"],
        "description": "Develop end-to-end web applications covering frontend and backend."
    },
    {
        "title": "Frontend Developer",
        "company_type": "Agency / Product",
        "salary": "₹4–12 LPA",
        "required_skills": ["HTML", "CSS", "JavaScript", "React", "TypeScript"],
        "description": "Build responsive and accessible user interfaces."
    },
    {
        "title": "Backend Developer",
        "company_type": "Enterprise / Startup",
        "salary": "₹5–14 LPA",
        "required_skills": ["Node.js", "Python", "SQL", "REST API", "Docker"],
        "description": "Design APIs, databases, and server-side application logic."
    },
    {
        "title": "Data Analyst",
        "company_type": "Finance / E-commerce",
        "salary": "₹4–10 LPA",
        "required_skills": ["SQL", "Excel", "Python", "Tableau", "Power BI"],
        "description": "Transform raw data into actionable business insights."
    },
    {
        "title": "DevOps Engineer",
        "company_type": "Enterprise / Cloud",
        "salary": "₹8–20 LPA",
        "required_skills": ["Linux", "Docker", "Kubernetes", "Jenkins", "AWS", "Terraform"],
        "description": "Automate CI/CD pipelines and manage cloud infrastructure."
    },
    {
        "title": "Cloud Engineer",
        "company_type": "IT / Consulting",
        "salary": "₹8–18 LPA",
        "required_skills": ["AWS", "Azure", "GCP", "Terraform", "Linux", "Python"],
        "description": "Architect and maintain cloud-based infrastructure and services."
    },
    {
        "title": "Cybersecurity Analyst",
        "company_type": "Finance / Government",
        "salary": "₹6–15 LPA",
        "required_skills": ["Networking", "Linux", "Python", "Ethical Hacking", "SIEM"],
        "description": "Protect systems and data from cyber threats."
    },
]


# ── Career Roadmaps ───────────────────────────────────────────
ROADMAPS = {
    "ai engineer": [
        {"step": 1, "phase": "Basics",
         "title": "Python & Math Foundations",
         "desc": "Learn Python, NumPy, Pandas. Study Linear Algebra and Statistics.",
         "resources": "CS50P, Khan Academy, Real Python"},
        {"step": 2, "phase": "Core Skills",
         "title": "Machine Learning Fundamentals",
         "desc": "Supervised/unsupervised learning, model evaluation, scikit-learn.",
         "resources": "Andrew Ng ML Course (Coursera), Kaggle Learn"},
        {"step": 3, "phase": "Advanced",
         "title": "Deep Learning & Frameworks",
         "desc": "TensorFlow, PyTorch, CNNs, RNNs, Transformers, and NLP.",
         "resources": "fast.ai, Deep Learning Specialisation, Hugging Face"},
        {"step": 4, "phase": "Projects",
         "title": "Build Portfolio Projects",
         "desc": "Build image classifier, chatbot, recommendation engine. Deploy with FastAPI.",
         "resources": "GitHub, Render, AWS EC2"},
        {"step": 5, "phase": "Apply",
         "title": "Certifications & Apply",
         "desc": "Earn Google ML Engineer or TensorFlow Developer cert. Apply on LinkedIn/Naukri.",
         "resources": "LeetCode, Pramp, LinkedIn, Naukri"},
    ],
    "data scientist": [
        {"step": 1, "phase": "Basics",
         "title": "Python & Statistics",
         "desc": "Python, Pandas, NumPy. Descriptive statistics and hypothesis testing.",
         "resources": "Codecademy, StatQuest (YouTube)"},
        {"step": 2, "phase": "Core Skills",
         "title": "Data Wrangling & Visualisation",
         "desc": "Data cleaning, Matplotlib, Seaborn, Tableau, Power BI.",
         "resources": "Kaggle, Tableau Public"},
        {"step": 3, "phase": "Advanced",
         "title": "ML & Big Data",
         "desc": "Apply ML models, advanced SQL, Spark, cloud data warehouses.",
         "resources": "Coursera Data Science Specialisation"},
        {"step": 4, "phase": "Apply",
         "title": "Certifications & Apply",
         "desc": "IBM Data Science or Google Data Analytics certificate.",
         "resources": "Coursera, LinkedIn, Naukri, Wellfound"},
    ],
    "full stack developer": [
        {"step": 1, "phase": "Basics",
         "title": "HTML, CSS & JavaScript",
         "desc": "Semantic HTML, CSS Flexbox/Grid, core JavaScript ES6+.",
         "resources": "freeCodeCamp, The Odin Project, MDN Web Docs"},
        {"step": 2, "phase": "Core Skills",
         "title": "React & Node.js",
         "desc": "Frontend with React, backend APIs with Node.js + Express.",
         "resources": "React docs, Express docs"},
        {"step": 3, "phase": "Database",
         "title": "MySQL & MongoDB",
         "desc": "Relational DB design with MySQL and NoSQL with MongoDB.",
         "resources": "MySQL Tutorial, MongoDB University"},
        {"step": 4, "phase": "Projects",
         "title": "Full Stack Apps",
         "desc": "Build 2 full-stack apps. Deploy on Vercel + Render.",
         "resources": "GitHub, Vercel, Render"},
        {"step": 5, "phase": "Apply",
         "title": "Apply & Interview Prep",
         "desc": "Practice system design and LeetCode. Apply on LinkedIn, Naukri.",
         "resources": "LeetCode, system-design-primer (GitHub)"},
    ],
}

GENERIC_ROADMAP = [
    {"step": 1, "phase": "Basics",
     "title": "Core Programming Fundamentals",
     "desc": "Learn programming basics and Computer Science fundamentals.",
     "resources": "CS50 (Harvard), freeCodeCamp, GeeksforGeeks"},
    {"step": 2, "phase": "Core Skills",
     "title": "Domain-Specific Skills",
     "desc": "Research and build proficiency in the key tools of your target role.",
     "resources": "Coursera, Udemy, official documentation"},
    {"step": 3, "phase": "Projects",
     "title": "Build Portfolio Projects",
     "desc": "Create 2–3 real projects and host them on GitHub.",
     "resources": "GitHub, Vercel, Render"},
    {"step": 4, "phase": "Certifications",
     "title": "Earn Certifications",
     "desc": "Get recognised certifications to validate your skills.",
     "resources": "Coursera, edX, LinkedIn Learning"},
    {"step": 5, "phase": "Apply",
     "title": "Network & Apply",
     "desc": "Update LinkedIn, write a targeted resume, apply consistently.",
     "resources": "LinkedIn, Naukri, Internshala, LeetCode"},
]


# ── Helper Functions ──────────────────────────────────────────
def parse_skills(skills_str):
    return [s.strip() for s in skills_str.split(",") if s.strip()]

def calc_match_score(user_skills, required_skills):
    user  = [s.lower() for s in user_skills]
    req   = [s.lower() for s in required_skills]
    if not req:
        return 0
    matched = [r for r in req if any(r in u or u in r for u in user)]
    return round((len(matched) / len(req)) * 100)

def get_recommendations(user_skills, top_n=6):
    scored = []
    for job in JOB_KB:
        score = calc_match_score(user_skills, job["required_skills"])
        if score > 0:
            scored.append({**job, "match_score": score})
    scored.sort(key=lambda x: x["match_score"], reverse=True)
    return scored[:top_n]

def get_roadmap(dream_job):
    d = dream_job.lower()
    for key, steps in ROADMAPS.items():
        if key in d or all(w in d for w in key.split()):
            return steps
    return GENERIC_ROADMAP

def skill_gap(user_skills, recommendations):
    all_required = list({
        s for job in recommendations
        for s in job["required_skills"]
    })
    user_lower = [s.lower() for s in user_skills]
    have    = [s for s in all_required if s.lower() in user_lower]
    missing = [s for s in all_required if s.lower() not in user_lower]
    return have, missing


# ── Navigation ────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
  <h1>🎯 Find Your <span>Dream Job</span></h1>
  <p>Enter your skills and goals — we'll build your personalized career roadmap</p>
</div>
""", unsafe_allow_html=True)

page = st.sidebar.selectbox(
    "📌 Navigate",
    ["🏠 Home", "🔍 Get Recommendations", "🗺️ Career Path"]
)


# ══════════════════════════════════════════════
# PAGE 1 — HOME
# ══════════════════════════════════════════════
if page == "🏠 Home":
    st.title("Welcome to CareerPath AI")
    st.write("This system helps students find jobs that match their skills "
             "and provides a step-by-step career roadmap.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("### 🎯 Dream Job Input\n\n"
                "Tell us your ultimate career goal and we'll tailor "
                "every recommendation to help you get there.")
    with col2:
        st.warning("### 📊 Skill Gap Analysis\n\n"
                   "We compare your current skills against market "
                   "requirements and highlight what you're missing.")
    with col3:
        st.success("### 🗺️ Career Path Guidance\n\n"
                   "Get a step-by-step plan from basics to advanced "
                   "skills and finally job applications.")

    st.markdown("---")
    st.markdown("### 💼 Jobs in Our Database")
    cols = st.columns(5)
    for i, job in enumerate(JOB_KB):
        with cols[i % 5]:
            st.markdown(f"**{job['title']}**  \n{job['salary']}")


# ══════════════════════════════════════════════
# PAGE 2 — GET RECOMMENDATIONS
# ══════════════════════════════════════════════
elif page == "🔍 Get Recommendations":
    st.title("📋 Get Job Recommendations")
    st.write("Fill in your profile below and we'll match you with the best job roles.")

    with st.form("profile_form"):
        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("👤 Full Name", placeholder="e.g. Ravi Kumar")
            skills_input = st.text_input(
                "🛠️ Current Skills (comma-separated)",
                placeholder="e.g. Python, Machine Learning, SQL"
            )
            experience = st.selectbox(
                "📅 Years of Experience",
                ["Fresher (0 years)", "1–2 years", "3–5 years", "5+ years"]
            )

        with col2:
            dream_job = st.text_input(
                "🌟 Dream Job Title",
                placeholder="e.g. AI Engineer, Data Scientist"
            )
            interests = st.text_area(
                "💡 Your Interests / Domains",
                placeholder="e.g. I enjoy working with data, building models...",
                height=120
            )

        submitted = st.form_submit_button("🔍 Get Recommendations", type="primary",
                                          use_container_width=True)

    if submitted:
        if not name or not skills_input or not dream_job:
            st.error("⚠️ Please fill in Name, Skills, and Dream Job.")
        else:
            user_skills = parse_skills(skills_input)

            # Save to session state for Career Path page
            st.session_state["name"]       = name
            st.session_state["skills"]     = user_skills
            st.session_state["dream_job"]  = dream_job
            st.session_state["experience"] = experience

            recommendations = get_recommendations(user_skills)
            st.session_state["recommendations"] = recommendations

            if not recommendations:
                st.warning("No matching jobs found. Try adding more skills.")
            else:
                st.success(f"✅ Found {len(recommendations)} job matches for you, {name}!")

                # ── Skill Gap Analysis ──
                st.markdown("---")
                st.subheader("📊 Skill Gap Analysis")
                have, missing = skill_gap(user_skills, recommendations)

                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**✅ Skills You Have**")
                    if have:
                        tags = "".join(
                            f'<span class="skill-have">{s}</span>' for s in have
                        )
                    else:
                        tags = "".join(
                            f'<span class="skill-have">{s}</span>' for s in user_skills
                        )
                    st.markdown(tags, unsafe_allow_html=True)

                with col2:
                    st.markdown("**⚠️ Skills to Acquire**")
                    if missing:
                        tags = "".join(
                            f'<span class="skill-missing">{s}</span>' for s in missing
                        )
                    else:
                        tags = '<span class="skill-have">Great match — no major gaps!</span>'
                    st.markdown(tags, unsafe_allow_html=True)

                # ── Job Cards ──
                st.markdown("---")
                st.subheader("💼 Recommended Jobs For You")

                for job in recommendations:
                    with st.container():
                        col1, col2 = st.columns([4, 1])
                        with col1:
                            st.markdown(f"### {job['title']}")
                            st.markdown(
                                f"🏢 **Company Type:** {job['company_type']}  "
                                f"&nbsp;&nbsp; 💰 **Salary:** {job['salary']}"
                            )
                            st.write(job["description"])
