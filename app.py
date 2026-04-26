import streamlit as st
import time
# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="CareerPath AI — Job Recommendation System",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)
# ─────────────────────────────────────────────
# FULL CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');
/* ── ROOT THEME ── */
:root {
    --navy:    #0d1b2a;
    --navy2:   #1b2d3f;
    --teal:    #00c9a7;
    --teal2:   #00a381;
    --red:     #e94560;
    --gold:    #f5a623;
    --white:   #f0f4f8;
    --muted:   #8a9bb0;
    --card-bg: #162032;
    --border:  rgba(0,201,167,0.18);
}
/* ── GLOBAL ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif !important;
    background-color: var(--navy) !important;
    color: var(--white) !important;
}
.stApp { background: var(--navy) !important; }
/* hide default streamlit elements */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 2.5rem 4rem !important; max-width: 1200px; }
/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: var(--navy2) !important;
    border-right: 1px solid var(--border);
}
[data-testid="stSidebar"] * { color: var(--white) !important; }
[data-testid="stSidebar"] .stSelectbox label {
    color: var(--muted) !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}
[data-testid="stSidebar"] [data-baseweb="select"] {
    background: var(--navy) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
}
/* ── HEADINGS ── */
h1, h2, h3, h4 {
    font-family: 'Sora', sans-serif !important;
    color: var(--white) !important;
}
/* ── HERO BANNER ── */
.hero-banner {
    background: linear-gradient(135deg, #0d1b2a 0%, #1a2f45 50%, #0d2233 100%);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 56px 48px;
    margin-bottom: 40px;
    position: relative;
    overflow: hidden;
}
.hero-banner::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 300px; height: 300px;
    background: radial-gradient(circle, rgba(0,201,167,0.12) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-banner::after {
    content: '';
    position: absolute;
    bottom: -80px; left: -40px;
    width: 250px; height: 250px;
    background: radial-gradient(circle, rgba(233,69,96,0.08) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-title {
    font-family: 'Sora', sans-serif;
    font-size: 3rem;
    font-weight: 800;
    line-height: 1.15;
    margin-bottom: 16px;
    color: var(--white);
}
.hero-title span { color: var(--teal); }
.hero-sub {
    font-size: 1.1rem;
    color: var(--muted);
    margin-bottom: 0;
    max-width: 500px;
    line-height: 1.7;
}
.hero-badge {
    display: inline-block;
    background: rgba(0,201,167,0.12);
    border: 1px solid rgba(0,201,167,0.3);
    color: var(--teal);
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 20px;
}
/* ── STAT CARDS ── */
.stat-row { display: flex; gap: 16px; margin-bottom: 32px; flex-wrap: wrap; }
.stat-card {
    flex: 1; min-width: 140px;
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 22px 20px;
    text-align: center;
}
.stat-num {
    font-family: 'Sora', sans-serif;
    font-size: 2rem;
    font-weight: 800;
    color: var(--teal);
    display: block;
}
.stat-label {
    font-size: 0.78rem;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.08em;
}
/* ── FEATURE CARDS ── */
.feature-grid { display: flex; gap: 20px; margin-bottom: 36px; flex-wrap: wrap; }
.feature-card {
    flex: 1; min-width: 220px;
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 28px 24px;
    transition: border-color 0.2s;
}
.feature-card:hover { border-color: var(--teal); }
.feature-icon { font-size: 2rem; margin-bottom: 14px; display: block; }
.feature-title {
    font-family: 'Sora', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    color: var(--white);
    margin-bottom: 8px;
}
.feature-desc { font-size: 0.88rem; color: var(--muted); line-height: 1.65; }
/* ── SECTION TITLE ── */
.section-title {
    font-family: 'Sora', sans-serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--white);
    margin-bottom: 6px;
}
.section-sub {
    font-size: 0.88rem;
    color: var(--muted);
    margin-bottom: 28px;
}
/* ── FORM CARD ── */
.form-card {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 36px;
    margin-bottom: 32px;
}
/* ── INPUTS ── */
.stTextInput input, .stTextArea textarea, .stSelectbox [data-baseweb="select"] {
    background: var(--navy) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    color: var(--white) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.95rem !important;
    padding: 12px 16px !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: var(--teal) !important;
    box-shadow: 0 0 0 3px rgba(0,201,167,0.1) !important;
}
.stTextInput label, .stTextArea label, .stSelectbox label {
    color: var(--muted) !important;
    font-size: 0.8rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.06em !important;
    text-transform: uppercase !important;
    margin-bottom: 6px !important;
}
/* ── BUTTONS ── */
.stButton button {
    background: linear-gradient(135deg, var(--teal), var(--teal2)) !important;
    color: var(--navy) !important;
    font-family: 'Sora', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 14px 32px !important;
    width: 100% !important;
    letter-spacing: 0.03em !important;
    transition: opacity 0.2s !important;
}
.stButton button:hover { opacity: 0.88 !important; }
/* ── JOB CARD ── */
.job-card {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 24px 28px;
    margin-bottom: 16px;
    position: relative;
    transition: border-color 0.2s;
}
.job-card:hover { border-color: var(--teal); }
.job-title {
    font-family: 'Sora', sans-serif;
    font-size: 1.15rem;
    font-weight: 700;
    color: var(--white);
    margin-bottom: 6px;
}
.job-meta {
    font-size: 0.84rem;
    color: var(--muted);
    margin-bottom: 10px;
}
.job-meta span { color: var(--teal); font-weight: 600; }
.job-desc { font-size: 0.9rem; color: #a0b0c0; line-height: 1.65; margin-bottom: 14px; }
.job-skills { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px; }
.skill-pill {
    background: rgba(0,201,167,0.08);
    border: 1px solid rgba(0,201,167,0.2);
    color: var(--teal);
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.78rem;
    font-weight: 500;
}
.skill-pill.missing {
    background: rgba(233,69,96,0.08);
    border-color: rgba(233,69,96,0.2);
    color: var(--red);
}
.match-badge {
    position: absolute;
    top: 24px; right: 24px;
    background: linear-gradient(135deg, var(--teal), var(--teal2));
    color: var(--navy);
    font-family: 'Sora', sans-serif;
    font-weight: 800;
    font-size: 0.9rem;
    padding: 6px 14px;
    border-radius: 20px;
}
.match-badge.high { background: linear-gradient(135deg, #00c9a7, #00a381); }
.match-badge.mid  { background: linear-gradient(135deg, #f5a623, #e0901a); color: white; }
.match-badge.low  { background: rgba(233,69,96,0.15); color: var(--red); border: 1px solid var(--red); }
/* ── SKILL GAP ── */
.gap-section {
    display: flex;
    gap: 20px;
    margin-bottom: 36px;
    flex-wrap: wrap;
}
.gap-box {
    flex: 1; min-width: 260px;
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 24px;
}
.gap-box.have   { border-color: rgba(0,201,167,0.3); }
.gap-box.missing{ border-color: rgba(233,69,96,0.3); }
.gap-box-title  {
    font-family: 'Sora', sans-serif;
    font-size: 0.85rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 16px;
}
.gap-box.have   .gap-box-title { color: var(--teal); }
.gap-box.missing .gap-box-title { color: var(--red); }
.tags { display: flex; flex-wrap: wrap; gap: 8px; }
.tag-have {
    background: rgba(0,201,167,0.1);
    border: 1px solid rgba(0,201,167,0.25);
    color: var(--teal);
    padding: 5px 13px; border-radius: 20px;
    font-size: 0.82rem; font-weight: 500;
}
.tag-miss {
    background: rgba(233,69,96,0.1);
    border: 1px solid rgba(233,69,96,0.25);
    color: var(--red);
    padding: 5px 13px; border-radius: 20px;
    font-size: 0.82rem; font-weight: 500;
}
/* ── CAREER STEPS ── */
.roadmap-step {
    display: flex;
    gap: 20px;
    margin-bottom: 24px;
    align-items: flex-start;
}
.step-num {
    width: 44px; height: 44px;
    background: linear-gradient(135deg, var(--teal), var(--teal2));
    color: var(--navy);
    font-family: 'Sora', sans-serif;
    font-weight: 800;
    font-size: 1rem;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
}
.step-body {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 20px 24px;
    flex: 1;
}
.step-phase {
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--teal);
    margin-bottom: 4px;
}
.step-title {
    font-family: 'Sora', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    color: var(--white);
    margin-bottom: 8px;
}
.step-desc { font-size: 0.88rem; color: #a0b0c0; line-height: 1.65; margin-bottom: 10px; }
.step-res  {
    font-size: 0.8rem;
    color: var(--muted);
    background: rgba(0,0,0,0.2);
    border-radius: 8px;
    padding: 8px 12px;
    border-left: 3px solid var(--teal);
}
/* ── PROGRESS BAR ── */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, var(--teal), var(--teal2)) !important;
    border-radius: 4px !important;
}
.stProgress > div > div { background: rgba(255,255,255,0.06) !important; border-radius: 4px !important; }
/* ── METRICS ── */
[data-testid="stMetricValue"] {
    font-family: 'Sora', sans-serif !important;
    color: var(--teal) !important;
    font-size: 2rem !important;
    font-weight: 800 !important;
}
[data-testid="stMetricLabel"] { color: var(--muted) !important; font-size: 0.78rem !important; }
/* ── ALERTS ── */
.stSuccess { background: rgba(0,201,167,0.08) !important; border-color: var(--teal) !important; color: var(--teal) !important; border-radius: 12px !important; }
.stWarning { background: rgba(245,166,35,0.08) !important; border-color: var(--gold) !important; border-radius: 12px !important; }
.stError   { background: rgba(233,69,96,0.08) !important; border-color: var(--red) !important; color: var(--red) !important; border-radius: 12px !important; }
.stInfo    { background: rgba(0,201,167,0.06) !important; border-color: rgba(0,201,167,0.3) !important; border-radius: 12px !important; }
/* ── DIVIDER ── */
hr { border-color: var(--border) !important; margin: 32px 0 !important; }
/* ── EXPANDER ── */
.streamlit-expanderHeader {
    background: var(--card-bg) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    color: var(--white) !important;
    font-family: 'Sora', sans-serif !important;
    font-weight: 600 !important;
}
.streamlit-expanderContent {
    background: var(--navy2) !important;
    border: 1px solid var(--border) !important;
    border-top: none !important;
    border-radius: 0 0 12px 12px !important;
}
/* ── JOB LIST ON HOME ── */
.job-list-item {
    display: flex; justify-content: space-between; align-items: center;
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 14px 20px;
    margin-bottom: 10px;
}
.job-list-name {
    font-family: 'Sora', sans-serif;
    font-size: 0.92rem;
    font-weight: 600;
    color: var(--white);
}
.job-list-salary {
    font-size: 0.82rem;
    color: var(--teal);
    font-weight: 600;
}
.job-list-type {
    font-size: 0.78rem;
    color: var(--muted);
}
/* ── SIDEBAR LOGO ── */
.sidebar-logo {
    font-family: 'Sora', sans-serif;
    font-size: 1.3rem;
    font-weight: 800;
    color: var(--teal);
    padding: 20px 0 8px;
    letter-spacing: -0.02em;
}
.sidebar-tagline {
    font-size: 0.78rem;
    color: var(--muted);
    margin-bottom: 24px;
    line-height: 1.5;
}
.sidebar-profile {
    background: rgba(0,201,167,0.06);
    border: 1px solid rgba(0,201,167,0.15);
    border-radius: 12px;
    padding: 16px;
    margin-top: 24px;
}
.sidebar-profile-name {
    font-family: 'Sora', sans-serif;
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--white);
    margin-bottom: 4px;
}
.sidebar-profile-detail {
    font-size: 0.78rem;
    color: var(--muted);
    line-height: 1.6;
}
/* ── SPINNER ── */
.stSpinner > div { border-top-color: var(--teal) !important; }
/* ── COLUMNS GAP ── */
[data-testid="column"] { padding: 0 8px !important; }
</style>
""", unsafe_allow_html=True)
# ─────────────────────────────────────────────
# DATA
# ─────────────────────────────────────────────
JOB_KB = [
    {"title": "AI Engineer",
     "company_type": "Tech / Product", "salary": "₹12–25 LPA",
     "required_skills": ["Python", "TensorFlow", "PyTorch", "Machine Learning", "Docker", "AWS"],
     "description": "Design, build, and deploy AI/ML models into production systems at scale.",
     "icon": "🤖"},
    {"title": "Data Scientist",
     "company_type": "Analytics / Consulting", "salary": "₹8–18 LPA",
     "required_skills": ["Python", "R", "SQL", "Statistics", "Pandas", "Tableau"],
     "description": "Analyse large datasets to extract insights and build predictive models.",
     "icon": "📊"},
    {"title": "Machine Learning Engineer",
     "company_type": "Startup / Enterprise", "salary": "₹10–20 LPA",
     "required_skills": ["Python", "scikit-learn", "Spark", "SQL", "Docker"],
     "description": "Build and maintain ML pipelines and model training infrastructure.",
     "icon": "⚙️"},
    {"title": "Full Stack Developer",
     "company_type": "Product / Service", "salary": "₹6–16 LPA",
     "required_skills": ["HTML", "CSS", "JavaScript", "Node.js", "React", "MySQL"],
     "description": "Develop end-to-end web applications covering frontend and backend.",
     "icon": "🌐"},
    {"title": "Frontend Developer",
     "company_type": "Agency / Product", "salary": "₹4–12 LPA",
     "required_skills": ["HTML", "CSS", "JavaScript", "React", "TypeScript"],
     "description": "Build responsive and accessible user interfaces for the web.",
     "icon": "🎨"},
    {"title": "Backend Developer",
     "company_type": "Enterprise / Startup", "salary": "₹5–14 LPA",
     "required_skills": ["Node.js", "Python", "SQL", "REST API", "Docker"],
     "description": "Design APIs, databases, and server-side application logic.",
     "icon": "🔧"},
    {"title": "Data Analyst",
     "company_type": "Finance / E-commerce", "salary": "₹4–10 LPA",
     "required_skills": ["SQL", "Excel", "Python", "Tableau", "Power BI"],
     "description": "Transform raw data into actionable business insights.",
     "icon": "📈"},
    {"title": "DevOps Engineer",
     "company_type": "Enterprise / Cloud", "salary": "₹8–20 LPA",
     "required_skills": ["Linux", "Docker", "Kubernetes", "Jenkins", "AWS", "Terraform"],
     "description": "Automate CI/CD pipelines and manage scalable cloud infrastructure.",
     "icon": "☁️"},
    {"title": "Cloud Engineer",
     "company_type": "IT / Consulting", "salary": "₹8–18 LPA",
     "required_skills": ["AWS", "Azure", "GCP", "Terraform", "Linux", "Python"],
     "description": "Architect and maintain cloud-based infrastructure and services.",
     "icon": "🌩️"},
    {"title": "Cybersecurity Analyst",
     "company_type": "Finance / Government", "salary": "₹6–15 LPA",
     "required_skills": ["Networking", "Linux", "Python", "Ethical Hacking", "SIEM"],
     "description": "Protect systems and data from cyber threats and vulnerabilities.",
     "icon": "🔐"},
    {"title": "Mobile App Developer",
     "company_type": "Product / Startup", "salary": "₹5–14 LPA",
     "required_skills": ["Flutter", "React Native", "Swift", "Kotlin", "Java", "Firebase"],
     "description": "Build dynamic and responsive mobile applications for iOS and Android.",
     "icon": "📱"},
    {"title": "Data Engineer",
     "company_type": "Enterprise / Big Data", "salary": "₹9–22 LPA",
     "required_skills": ["Python", "SQL", "Spark", "Airflow", "AWS", "Hadoop"],
     "description": "Design and build data pipelines, architectures, and data warehouses.",
     "icon": "🏗️"},
    {"title": "Blockchain Developer",
     "company_type": "Web3 / Finance", "salary": "₹10–25 LPA",
     "required_skills": ["Solidity", "Rust", "Ethereum", "Smart Contracts", "Cryptography", "Node.js"],
     "description": "Develop decentralized applications (dApps) and smart contracts.",
     "icon": "⛓️"},
    {"title": "UI/UX Designer",
     "company_type": "Agency / Product", "salary": "₹4–12 LPA",
     "required_skills": ["Figma", "Adobe XD", "User Research", "Wireframing", "Prototyping", "CSS"],
     "description": "Create intuitive and beautiful user interfaces and experiences.",
     "icon": "✨"},
    {"title": "QA Automation Engineer",
     "company_type": "Enterprise / Product", "salary": "₹5–13 LPA",
     "required_skills": ["Selenium", "Cypress", "Python", "Java", "Postman", "CI/CD"],
     "description": "Design and implement automated testing frameworks for software quality.",
     "icon": "🧪"},
]
ROADMAPS = {
    "ai engineer": [
        {"step": 1, "phase": "Basics",
         "title": "Python & Math Foundations",
         "desc": "Learn Python, NumPy, Pandas. Study Linear Algebra, Statistics, and Probability — these underpin every ML algorithm.",
         "resources": "CS50P (Harvard), Khan Academy Math, Real Python"},
        {"step": 2, "phase": "Core Skills",
         "title": "Machine Learning Fundamentals",
         "desc": "Master supervised and unsupervised learning, model evaluation, cross-validation, and scikit-learn workflows.",
         "resources": "Andrew Ng ML Course (Coursera), Kaggle Learn"},
        {"step": 3, "phase": "Advanced",
         "title": "Deep Learning & Frameworks",
         "desc": "Study TensorFlow, PyTorch, CNNs, RNNs, Transformers, and NLP. Build and fine-tune neural networks.",
         "resources": "fast.ai, Deep Learning Specialisation, Hugging Face docs"},
        {"step": 4, "phase": "Projects",
         "title": "Build & Deploy Portfolio Projects",
         "desc": "Build an image classifier, chatbot, and recommendation engine. Deploy with FastAPI on a cloud server.",
         "resources": "GitHub, Render, AWS EC2 Free Tier"},
        {"step": 5, "phase": "MLOps",
         "title": "Production & MLOps",
         "desc": "Learn Docker, MLflow, CI/CD pipelines, and cloud ML services like AWS SageMaker or GCP Vertex AI.",
         "resources": "Full Stack Deep Learning, MLflow docs, Docker docs"},
        {"step": 6, "phase": "Apply",
         "title": "Certifications & Job Applications",
         "desc": "Earn Google ML Engineer or TensorFlow Developer cert. Practice LeetCode and apply on LinkedIn and Naukri.",
         "resources": "LeetCode, Pramp, LinkedIn, Naukri"},
    ],
    "data scientist": [
        {"step": 1, "phase": "Basics",
         "title": "Python & Statistics",
         "desc": "Learn Python, Pandas, NumPy. Study descriptive statistics, probability distributions, and hypothesis testing.",
         "resources": "Codecademy Python, StatQuest (YouTube), Think Stats"},
        {"step": 2, "phase": "Core Skills",
         "title": "Data Wrangling & Visualisation",
         "desc": "Master data cleaning, feature engineering, Matplotlib, Seaborn, and Tableau or Power BI.",
         "resources": "Kaggle, Tableau Public, freeCodeCamp"},
        {"step": 3, "phase": "Advanced",
         "title": "Machine Learning & Big Data",
         "desc": "Apply ML algorithms, advanced SQL analytics, Apache Spark, and cloud data warehouses like BigQuery.",
         "resources": "Coursera Data Science Specialisation, Spark docs"},
        {"step": 4, "phase": "Projects",
         "title": "End-to-End Projects",
         "desc": "Build EDA reports, predictive models, and live dashboards. Publish on Kaggle and GitHub.",
         "resources": "Kaggle Competitions, GitHub, Streamlit (for dashboards)"},
        {"step": 5, "phase": "Apply",
         "title": "Certifications & Apply",
         "desc": "Earn IBM Data Science Professional or Google Data Analytics certificate. Start applying.",
         "resources": "Coursera, LinkedIn, Naukri, Wellfound"},
    ],
    "full stack developer": [
        {"step": 1, "phase": "Basics",
         "title": "HTML, CSS & JavaScript",
         "desc": "Master semantic HTML5, CSS Flexbox and Grid, and core JavaScript ES6+ concepts.",
         "resources": "freeCodeCamp, The Odin Project, MDN Web Docs"},
        {"step": 2, "phase": "Frontend",
         "title": "React.js",
         "desc": "Build dynamic UIs with React — components, hooks, state management with Redux or Context API.",
         "resources": "React official docs, Scrimba React Course"},
        {"step": 3, "phase": "Backend",
         "title": "Node.js & Express",
         "desc": "Build REST APIs with Node.js and Express. Learn middleware, authentication, and error handling.",
         "resources": "Express docs, The Odin Project Node"},
        {"step": 4, "phase": "Database",
         "title": "MySQL & MongoDB",
         "desc": "Design relational databases with MySQL and work with NoSQL using MongoDB.",
         "resources": "MySQL Tutorial, MongoDB University (free)"},
        {"step": 5, "phase": "Projects",
         "title": "Full Stack Apps",
         "desc": "Build 2 complete apps (e.g. e-commerce, task manager). Deploy frontend on Vercel, backend on Render.",
         "resources": "GitHub, Vercel, Render"},
        {"step": 6, "phase": "Apply",
         "title": "Advanced Skills & Apply",
         "desc": "Add TypeScript, Docker basics, and CI/CD. Practice system design and apply on LinkedIn and Naukri.",
         "resources": "TypeScript Handbook, LeetCode, system-design-primer (GitHub)"},
    ],
    "machine learning engineer": [
        {"step": 1, "phase": "Basics", "title": "Math & Python", "desc": "Learn Python, Linear Algebra, Calculus, and Statistics.", "resources": "Khan Academy, Python Docs"},
        {"step": 2, "phase": "Core Skills", "title": "Classical ML", "desc": "Master scikit-learn, regression, classification, and clustering.", "resources": "Coursera"},
        {"step": 3, "phase": "Advanced", "title": "Deep Learning", "desc": "Learn PyTorch or TensorFlow for neural networks.", "resources": "DeepLearning.AI"},
        {"step": 4, "phase": "Projects", "title": "ML Projects", "desc": "Build an image classifier or recommender system.", "resources": "Kaggle"},
        {"step": 5, "phase": "MLOps", "title": "Deployment", "desc": "Deploy models using Docker, FastAPI, and MLflow.", "resources": "MLflow Docs"},
        {"step": 6, "phase": "Apply", "title": "Job Search", "desc": "Update resume with ML projects and practice interviews.", "resources": "LinkedIn, Naukri"},
    ],
    "frontend developer": [
        {"step": 1, "phase": "Basics", "title": "HTML, CSS, JS", "desc": "Understand DOM, Flexbox, Grid, and ES6 Javascript.", "resources": "MDN Web Docs, freeCodeCamp"},
        {"step": 2, "phase": "Framework", "title": "Learn React", "desc": "Master components, hooks, and basic state management.", "resources": "React Docs"},
        {"step": 3, "phase": "Styling", "title": "Modern Styling", "desc": "Learn Tailwind CSS or Styled Components.", "resources": "Tailwind Labs"},
        {"step": 4, "phase": "Advanced", "title": "TypeScript & Next.js", "desc": "Add static typing and learn server-side rendering.", "resources": "Next.js Docs"},
        {"step": 5, "phase": "Projects", "title": "Build UI Clones", "desc": "Clone Spotify or Netflix UI.", "resources": "Frontend Mentor"},
        {"step": 6, "phase": "Apply", "title": "Portfolio & Apply", "desc": "Host on Vercel and apply for frontend roles.", "resources": "Vercel, LinkedIn"},
    ],
    "backend developer": [
        {"step": 1, "phase": "Basics", "title": "Programming & Web", "desc": "Learn Node.js or Python, HTTP, and REST principles.", "resources": "MDN, Python docs"},
        {"step": 2, "phase": "Databases", "title": "SQL & NoSQL", "desc": "Learn MySQL/PostgreSQL and MongoDB schemas.", "resources": "MongoDB University"},
        {"step": 3, "phase": "Framework", "title": "Express or Django", "desc": "Build APIs, middleware, and authentication.", "resources": "Django Docs"},
        {"step": 4, "phase": "Architecture", "title": "Caching & Queues", "desc": "Implement Redis caching and background jobs.", "resources": "Redis Docs"},
        {"step": 5, "phase": "DevOps", "title": "Docker & Deployment", "desc": "Containerize apps and deploy to AWS or Render.", "resources": "Docker Docs"},
        {"step": 6, "phase": "Apply", "title": "System Design & Apply", "desc": "Study basic system design and start applying.", "resources": "ByteByteGo"},
    ],
    "data analyst": [
        {"step": 1, "phase": "Basics", "title": "Excel Basics", "desc": "Master advanced Excel functions, VLOOKUP, pivot tables.", "resources": "Excelisfun (YouTube)"},
        {"step": 2, "phase": "Core Skills", "title": "SQL Mastery", "desc": "Learn joins, aggregations, and window functions.", "resources": "Mode Analytics SQL"},
        {"step": 3, "phase": "Tools", "title": "BI Tools", "desc": "Create dashboards in Tableau or Power BI.", "resources": "Tableau Public"},
        {"step": 4, "phase": "Programming", "title": "Python for Data", "desc": "Learn Pandas and Matplotlib for data wrangling.", "resources": "Kaggle"},
        {"step": 5, "phase": "Projects", "title": "Analyst Portfolio", "desc": "Analyze public datasets and publish dashboards.", "resources": "Maven Analytics"},
        {"step": 6, "phase": "Apply", "title": "Certifications", "desc": "Get Google Data Analytics cert and apply.", "resources": "Coursera"},
    ],
    "devops engineer": [
        {"step": 1, "phase": "Basics", "title": "Linux & Bash", "desc": "Learn Linux commands, scripting, and networking.", "resources": "Linux Journey"},
        {"step": 2, "phase": "Core Skills", "title": "Version Control & CI/CD", "desc": "Master Git and setup GitHub Actions or Jenkins.", "resources": "GitHub Docs"},
        {"step": 3, "phase": "Containers", "title": "Docker", "desc": "Build and run multi-container applications.", "resources": "Docker Docs"},
        {"step": 4, "phase": "Orchestration", "title": "Kubernetes", "desc": "Learn K8s architecture, pods, and deployments.", "resources": "Kubernetes Docs"},
        {"step": 5, "phase": "Infrastructure", "title": "Terraform & Cloud", "desc": "Use IaC to provision AWS or Azure resources.", "resources": "HashiCorp Docs"},
        {"step": 6, "phase": "Apply", "title": "Certifications", "desc": "AWS Solutions Architect or CKA. Apply for roles.", "resources": "A Cloud Guru"},
    ],
    "cloud engineer": [
        {"step": 1, "phase": "Basics", "title": "Networking & IT", "desc": "Understand DNS, TCP/IP, VPCs, and Firewalls.", "resources": "NetworkChuck"},
        {"step": 2, "phase": "Core Platform", "title": "AWS / Azure Basics", "desc": "Learn core compute, storage, and IAM services.", "resources": "AWS Skill Builder"},
        {"step": 3, "phase": "Automation", "title": "IaC & Scripting", "desc": "Write Python automation scripts and Terraform.", "resources": "Terraform Docs"},
        {"step": 4, "phase": "Advanced", "title": "Cloud Architecture", "desc": "Design highly available and scalable systems.", "resources": "AWS Well-Architected Framework"},
        {"step": 5, "phase": "Projects", "title": "Cloud Resume Challenge", "desc": "Host a resume using S3, CloudFront, API Gateway, DynamoDB.", "resources": "Cloud Resume Challenge"},
        {"step": 6, "phase": "Apply", "title": "Certifications", "desc": "AWS SysOps or Developer Associate. Apply.", "resources": "LinkedIn"},
    ],
    "cybersecurity analyst": [
        {"step": 1, "phase": "Basics", "title": "Networking & OS", "desc": "Deep dive into OSI model, TCP/IP, and Linux internals.", "resources": "Professor Messer"},
        {"step": 2, "phase": "Core Skills", "title": "Security Fundamentals", "desc": "Learn OWASP Top 10, cryptography, access controls.", "resources": "TryHackMe"},
        {"step": 3, "phase": "Defensive", "title": "Blue Team & SIEM", "desc": "Monitor logs with Splunk, analyze network traffic with Wireshark.", "resources": "Splunk Training"},
        {"step": 4, "phase": "Offensive", "title": "Ethical Hacking", "desc": "Understand vulnerabilities and run basic pentests.", "resources": "HackTheBox"},
        {"step": 5, "phase": "Projects", "title": "Home Lab", "desc": "Set up pfSense and an Active Directory lab.", "resources": "YouTube"},
        {"step": 6, "phase": "Apply", "title": "Certifications", "desc": "Get CompTIA Security+ and apply for SOC Analyst roles.", "resources": "CompTIA"},
    ],
    "mobile app developer": [
        {"step": 1, "phase": "Basics", "title": "Programming Basics", "desc": "Learn Dart for Flutter or JavaScript for React Native.", "resources": "Dart.dev / MDN"},
        {"step": 2, "phase": "Framework", "title": "UI & Components", "desc": "Build interactive screens, navigation, and layouts.", "resources": "Official Docs"},
        {"step": 3, "phase": "State", "title": "State Management", "desc": "Learn Provider/Riverpod (Flutter) or Redux (RN).", "resources": "Official Docs"},
        {"step": 4, "phase": "Backend", "title": "Firebase & APIs", "desc": "Integrate REST APIs, Firebase Auth, and Firestore.", "resources": "Firebase Docs"},
        {"step": 5, "phase": "Projects", "title": "App Clones", "desc": "Build a WhatsApp or Instagram clone.", "resources": "GitHub"},
        {"step": 6, "phase": "Apply", "title": "App Store & Apply", "desc": "Publish an app to Google Play and apply for jobs.", "resources": "Google Play Console"},
    ],
    "data engineer": [
        {"step": 1, "phase": "Basics", "title": "Python & Advanced SQL", "desc": "Master Python data structures and complex SQL queries.", "resources": "LeetCode"},
        {"step": 2, "phase": "Core Skills", "title": "Data Warehousing", "desc": "Learn dimensional modeling and Snowflake/BigQuery.", "resources": "Kimball Methodology"},
        {"step": 3, "phase": "Processing", "title": "Spark & Big Data", "desc": "Process large datasets using Apache Spark.", "resources": "Databricks Connect"},
        {"step": 4, "phase": "Orchestration", "title": "Airflow", "desc": "Schedule and monitor data pipelines using Apache Airflow.", "resources": "Airflow Docs"},
        {"step": 5, "phase": "Projects", "title": "End-to-End Pipeline", "desc": "Ingest API data, process in Spark, load to Snowflake.", "resources": "GitHub"},
        {"step": 6, "phase": "Apply", "title": "Interview Prep", "desc": "Prepare for SQL and system design interviews. Apply.", "resources": "Data Interview Pro"},
    ],
    "blockchain developer": [
        {"step": 1, "phase": "Basics", "title": "Blockchain Fundamentals", "desc": "Understand hashing, consensus, cryptography.", "resources": "Bitcoin Whitepaper"},
        {"step": 2, "phase": "Core Skills", "title": "Solidity", "desc": "Learn Solidity to write smart contracts on Ethereum.", "resources": "CryptoZombies"},
        {"step": 3, "phase": "Tools", "title": "Hardhat & Web3.js", "desc": "Test and deploy contracts. Connect frontend with Web3.js.", "resources": "Hardhat Docs"},
        {"step": 4, "phase": "Advanced", "title": "Security & DeFi", "desc": "Learn reentrancy attacks, DeFi protocols like Uniswap.", "resources": "Docs"},
        {"step": 5, "phase": "Projects", "title": "Build a dApp", "desc": "Create an NFT marketplace or a staking dApp.", "resources": "Buildspace"},
        {"step": 6, "phase": "Apply", "title": "Web3 Bounties", "desc": "Participate in hackathons, complete bounties, and apply.", "resources": "Gitcoin"},
    ],
    "ui/ux designer": [
        {"step": 1, "phase": "Basics", "title": "Design Principles", "desc": "Learn typography, color theory, layout, and contrast.", "resources": "Refactoring UI"},
        {"step": 2, "phase": "Tools", "title": "Figma Mastery", "desc": "Master auto-layout, components, and variables in Figma.", "resources": "Figma Tutorials"},
        {"step": 3, "phase": "UX", "title": "User Research", "desc": "Learn wireframing, user flows, personas, and usability testing.", "resources": "NNGroup"},
        {"step": 4, "phase": "Advanced", "title": "Prototyping", "desc": "Create high-fidelity interactive prototypes with animations.", "resources": "Figma Docs"},
        {"step": 5, "phase": "Projects", "title": "Case Studies", "desc": "Redesign a poorly designed app and justify your choices.", "resources": "Behance"},
        {"step": 6, "phase": "Apply", "title": "Portfolio Presentation", "desc": "Build a portfolio site and apply for roles.", "resources": "Dribbble"},
    ],
    "qa automation engineer": [
        {"step": 1, "phase": "Basics", "title": "Manual Testing", "desc": "Learn test cases, bug reporting, and STLC.", "resources": "Guru99"},
        {"step": 2, "phase": "Programming", "title": "Java or Python", "desc": "Learn core programming for automation scripts.", "resources": "Codecademy"},
        {"step": 3, "phase": "Core UI", "title": "Selenium & Cypress", "desc": "Automate web browser testing.", "resources": "Cypress Docs"},
        {"step": 4, "phase": "API", "title": "API Testing", "desc": "Learn Postman, REST Assured, and JSON.", "resources": "Postman Learning Center"},
        {"step": 5, "phase": "DevOps", "title": "CI/CD Integration", "desc": "Run automated tests in Jenkins or GitHub Actions.", "resources": "GitHub Docs"},
        {"step": 6, "phase": "Apply", "title": "Projects & Apply", "desc": "Build a test framework from scratch and apply.", "resources": "LinkedIn"},
    ],
}
GENERIC_ROADMAP = [
    {"step": 1, "phase": "Basics",
     "title": "Core Programming Fundamentals",
     "desc": "Learn a programming language (Python recommended) and Computer Science fundamentals.",
     "resources": "CS50 (Harvard), freeCodeCamp, GeeksforGeeks"},
    {"step": 2, "phase": "Core Skills",
     "title": "Domain-Specific Tools",
     "desc": "Research and build proficiency in the key tools and languages used in your target role.",
     "resources": "Coursera, Udemy, official documentation"},
    {"step": 3, "phase": "Projects",
     "title": "Build Portfolio Projects",
     "desc": "Create 2–3 real projects demonstrating your skills. Host them on GitHub.",
     "resources": "GitHub, Vercel, Render, AWS Free Tier"},
    {"step": 4, "phase": "Certifications",
     "title": "Earn Certifications",
     "desc": "Pursue recognised industry certifications to validate your skills for employers.",
     "resources": "Coursera, edX, LinkedIn Learning"},
    {"step": 5, "phase": "Network",
     "title": "Build Network & Apply",
     "desc": "Update LinkedIn, write a targeted resume, and apply 5–10 jobs per week consistently.",
     "resources": "LinkedIn, Naukri, Internshala, Wellfound"},
    {"step": 6, "phase": "Interview",
     "title": "Interview Prep & Land the Job",
     "desc": "Practice DSA, system design, and role-specific questions. Do mock interviews.",
     "resources": "LeetCode, HackerRank, Pramp, InterviewBit"},
]
# ─────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────
def parse_skills(s):
    return [x.strip() for x in s.split(",") if x.strip()]
def calc_score(user_skills, required):
    u = [s.lower() for s in user_skills]
    r = [s.lower() for s in required]
    if not r:
        return 0
    matched = [x for x in r if any(x in y or y in x for y in u)]
    return round(len(matched) / len(r) * 100)
def get_recommendations(user_skills, n=6):
    scored = []
    for job in JOB_KB:
        sc = calc_score(user_skills, job["required_skills"])
        if sc > 0:
            scored.append({**job, "score": sc})
    return sorted(scored, key=lambda x: x["score"], reverse=True)[:n]
def get_roadmap(dream_job):
    d = dream_job.lower()
    for key, steps in ROADMAPS.items():
        if key in d or all(w in d for w in key.split()):
            return steps
    return GENERIC_ROADMAP
def skill_gap(user_skills, recs):
    all_req = list({s for j in recs for s in j["required_skills"]})
    u = [s.lower() for s in user_skills]
    have    = [s for s in all_req if s.lower() in u]
    missing = [s for s in all_req if s.lower() not in u]
    return have, missing
def badge_class(score):
    if score >= 70: return "high"
    if score >= 40: return "mid"
    return "low"
# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-logo">🎯 CareerPath AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-tagline">Personalized job recommendations<br>powered by skill matching</div>', unsafe_allow_html=True)
    page = st.selectbox(
        "NAVIGATE",
        ["🏠  Home", "🔍  Get Recommendations", "🗺️  Career Path", "📊  All Jobs"],
        label_visibility="visible"
    )
    # Show saved profile if exists
    if "name" in st.session_state:
        st.markdown(f"""
        <div class="sidebar-profile">
            <div class="sidebar-profile-name">👤 {st.session_state.name}</div>
            <div class="sidebar-profile-detail">
                🌟 {st.session_state.get('dream_job','—')}<br>
                🛠️ {len(st.session_state.get('skills', []))} skills added<br>
                📅 {st.session_state.get('experience','—')}
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("---")
    st.markdown('<div style="font-size:0.75rem;color:var(--muted);line-height:1.7;">Built with Python & Streamlit<br>Job Recommendation System<br>© 2025 CareerPath AI</div>', unsafe_allow_html=True)
# ─────────────────────────────────────────────
# PAGE: HOME
# ─────────────────────────────────────────────
if "Home" in page:
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-badge">🚀 AI-Powered Career Guidance</div>
        <div class="hero-title">Find Your <span>Dream Job</span><br>with Smart Matching</div>
        <div class="hero-sub">Enter your skills and career goals — we analyse your profile,
        identify skill gaps, and build a personalised step-by-step roadmap to get you hired.</div>
    </div>
    """, unsafe_allow_html=True)
    # Stats row
    st.markdown("""
    <div class="stat-row">
        <div class="stat-card"><span class="stat-num">15</span><span class="stat-label">Job Roles</span></div>
        <div class="stat-card"><span class="stat-num">60+</span><span class="stat-label">Skills Tracked</span></div>
        <div class="stat-card"><span class="stat-num">15</span><span class="stat-label">Career Roadmaps</span></div>
        <div class="stat-card"><span class="stat-num">100%</span><span class="stat-label">Free to Use</span></div>
    </div>
    """, unsafe_allow_html=True)
    # Features
    st.markdown("""
    <div class="feature-grid">
        <div class="feature-card">
            <span class="feature-icon">🎯</span>
            <div class="feature-title">Dream Job Input</div>
            <div class="feature-desc">Tell us your ultimate career goal and we'll tailor every recommendation to help you get there.</div>
        </div>
        <div class="feature-card">
            <span class="feature-icon">📊</span>
            <div class="feature-title">Skill Gap Analysis</div>
            <div class="feature-desc">We compare your current skills against market requirements and highlight exactly what you're missing.</div>
        </div>
        <div class="feature-card">
            <span class="feature-icon">🗺️</span>
            <div class="feature-title">Career Path Guidance</div>
            <div class="feature-desc">Get a step-by-step roadmap from basics to advanced skills and finally job applications.</div>
        </div>
        <div class="feature-card">
            <span class="feature-icon">⚡</span>
            <div class="feature-title">Instant Results</div>
            <div class="feature-desc">No waiting. Get your personalised job matches and career roadmap in seconds.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    # How it works
    st.markdown("---")
    st.markdown('<div class="section-title">How It Works</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Three simple steps to your dream career</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="step-body" style="text-align:center; padding:32px 24px;">
            <div style="font-size:2.5rem; margin-bottom:16px;">📝</div>
            <div class="step-phase">Step 1</div>
            <div class="step-title">Enter Your Profile</div>
            <div class="step-desc">Add your name, current skills, experience level, and dream job title.</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="step-body" style="text-align:center; padding:32px 24px;">
            <div style="font-size:2.5rem; margin-bottom:16px;">🔍</div>
            <div class="step-phase">Step 2</div>
            <div class="step-title">Get Matched</div>
            <div class="step-desc">Our algorithm scores every job against your skills and shows the best matches.</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="step-body" style="text-align:center; padding:32px 24px;">
            <div style="font-size:2.5rem; margin-bottom:16px;">🚀</div>
            <div class="step-phase">Step 3</div>
            <div class="step-title">Follow Your Roadmap</div>
            <div class="step-desc">Get your personalised career path with resources for every stage.</div>
        </div>""", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown('<div class="section-title">Available Job Roles</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">We match your skills against these 15 in-demand roles</div>', unsafe_allow_html=True)
    for job in JOB_KB:
        st.markdown(f"""
        <div class="job-list-item">
            <div>
                <span style="font-size:1.1rem; margin-right:10px;">{job['icon']}</span>
                <span class="job-list-name">{job['title']}</span>
                <span class="job-list-type" style="margin-left:12px;">· {job['company_type']}</span>
            </div>
            <span class="job-list-salary">{job['salary']}</span>
        </div>
        """, unsafe_allow_html=True)
# ─────────────────────────────────────────────
# PAGE: GET RECOMMENDATIONS
# ─────────────────────────────────────────────
elif "Recommendations" in page:
    st.markdown("""
    <div class="hero-banner" style="padding:36px 40px;">
        <div class="hero-title" style="font-size:2rem;">🔍 Get Job Recommendations</div>
        <div class="hero-sub" style="font-size:0.95rem;">
            Fill in your profile — we'll match you with the best roles and show your skill gaps
        </div>
    </div>
    """, unsafe_allow_html=True)
    # ── Input Form ──
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title" style="font-size:1.1rem; margin-bottom:4px;">Your Profile</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">All fields marked with * are required</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("👤 Full Name *", placeholder="e.g. Ravi Kumar",
                             value=st.session_state.get("name", ""))
        skills_input = st.text_input("🛠️ Current Skills * (comma-separated)",
                                     placeholder="e.g. Python, Machine Learning, SQL",
                                     value=", ".join(st.session_state.get("skills", [])))
        experience = st.selectbox("📅 Years of Experience",
                                  ["Fresher (0 years)", "1–2 years", "3–5 years", "5+ years"],
                                  index=["Fresher (0 years)", "1–2 years", "3–5 years", "5+ years"].index(
                                      st.session_state.get("experience", "Fresher (0 years)")))
    with col2:
        dream_job = st.text_input("🌟 Dream Job Title *",
                                  placeholder="e.g. AI Engineer, Data Scientist",
                                  value=st.session_state.get("dream_job", ""))
        interests = st.text_area("💡 Interests / Domains (optional)",
                                 placeholder="e.g. I enjoy building ML models and solving data problems...",
                                 height=130,
                                 value=st.session_state.get("interests", ""))
    st.markdown('</div>', unsafe_allow_html=True)
    clicked = st.button("🔍  Analyse My Profile & Get Recommendations", type="primary")
    if clicked:
        if not name.strip() or not skills_input.strip() or not dream_job.strip():
            st.error("⚠️ Please fill in Name, Skills, and Dream Job Title.")
        else:
            user_skills = parse_skills(skills_input)
            # Save to session
            st.session_state.name        = name.strip()
            st.session_state.skills      = user_skills
            st.session_state.dream_job   = dream_job.strip()
            st.session_state.experience  = experience
            st.session_state.interests   = interests
            with st.spinner("Analysing your profile..."):
                time.sleep(0.6)
                recs = get_recommendations(user_skills)
                st.session_state.recommendations = recs
    # ── Show Results if available ──
    if "recommendations" in st.session_state and st.session_state.recommendations:
        recs        = st.session_state.recommendations
        user_skills = st.session_state.get("skills", [])
        name        = st.session_state.get("name", "")
        dream_job   = st.session_state.get("dream_job", "")
        st.success(f"✅ Found {len(recs)} job matches for **{name}** — sorted by best match!")
        # ── Skill Gap ──
        st.markdown("---")
        st.markdown('<div class="section-title">📊 Skill Gap Analysis</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-sub">Your current skills vs. what the market needs</div>', unsafe_allow_html=True)
        have, missing = skill_gap(user_skills, recs)
        have_tags    = "".join(f'<span class="tag-have">{s}</span>'    for s in (have    or user_skills))
        missing_tags = "".join(f'<span class="tag-miss">{s}</span>'    for s in missing) if missing else '<span class="tag-have">No major gaps — great match!</span>'
        st.markdown(f"""
        <div class="gap-section">
            <div class="gap-box have">
                <div class="gap-box-title">✅ Skills You Have ({len(have or user_skills)})</div>
                <div class="tags">{have_tags}</div>
            </div>
            <div class="gap-box missing">
                <div class="gap-box-title">⚠️ Skills to Acquire ({len(missing)})</div>
                <div class="tags">{missing_tags}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        # ── Metrics row ──
        avg_score = round(sum(j["score"] for j in recs) / len(recs))
        top_score = recs[0]["score"]
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Top Match",        f"{top_score}%")
        c2.metric("Avg Match",        f"{avg_score}%")
        c3.metric("Jobs Found",       len(recs))
        c4.metric("Skills You Have",  len(have or user_skills))
        # ── Job Cards ──
        st.markdown("---")
        st.markdown('<div class="section-title">💼 Recommended Jobs For You</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="section-sub">Matched to your skills for the role of <strong style="color:var(--teal)">{dream_job}</strong></div>', unsafe_allow_html=True)
        user_lower = [s.lower() for s in user_skills]
        for job in recs:
            bc = badge_class(job["score"])
            skill_pills = ""
            for s in job["required_skills"]:
                css = "skill-pill" if s.lower() in user_lower else "skill-pill missing"
                skill_pills += f'<span class="{css}">{s}</span>'
            st.markdown(f"""
            <div class="job-card">
                <span class="match-badge {bc}">{job['score']}% Match</span>
                <div class="job-title">{job['icon']}  {job['title']}</div>
                <div class="job-meta">
                    🏢 {job['company_type']} &nbsp;·&nbsp;
                    💰 <span>{job['salary']}</span>
                </div>
                <div class="job-desc">{job['description']}</div>
                <div class="job-skills">{skill_pills}</div>
                <div style="font-size:0.73rem; color:var(--muted); margin-top:10px;">
                    🟢 Green = you have it &nbsp;·&nbsp; 🔴 Red = you need it
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("---")
        st.info("👉 Navigate to **Career Path** in the sidebar to see your step-by-step roadmap!")
# ─────────────────────────────────────────────
# PAGE: CAREER PATH
# ─────────────────────────────────────────────
elif "Career Path" in page:
    if "dream_job" not in st.session_state:
        st.markdown("""
        <div class="hero-banner">
            <div class="hero-title" style="font-size:1.8rem;">🗺️ Career Roadmap</div>
            <div class="hero-sub">No profile found. Please go to
            <strong style="color:var(--teal)">Get Recommendations</strong>
            first and fill in your details.</div>
        </div>
        """, unsafe_allow_html=True)
        st.stop()
    name      = st.session_state.name
    dream_job = st.session_state.dream_job
    skills    = st.session_state.skills
    st.markdown(f"""
    <div class="hero-banner" style="padding:36px 40px;">
        <div class="hero-badge">🗺️ Personalised Roadmap</div>
        <div class="hero-title" style="font-size:2rem;">{name}'s Path to<br><span>{dream_job}</span></div>
        <div class="hero-sub" style="font-size:0.92rem;">
            Follow these steps consistently — each one builds on the last.
        </div>
    </div>
    """, unsafe_allow_html=True)
    # Progress
    progress = min(len(skills) * 8, 100)
    st.markdown(f'<div style="font-size:0.82rem; color:var(--muted); margin-bottom:6px; text-transform:uppercase; letter-spacing:0.08em;">Profile Strength — based on {len(skills)} skills added</div>', unsafe_allow_html=True)
    st.progress(progress)
    st.markdown(f'<div style="font-size:0.8rem; color:var(--teal); margin-bottom:28px;">{progress}% complete — keep adding skills to improve your match score</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown('<div class="section-title">Your Step-by-Step Roadmap</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Tailored for your dream role — from basics to job applications</div>', unsafe_allow_html=True)
    roadmap = get_roadmap(dream_job)
    for step in roadmap:
        st.markdown(f"""
        <div class="roadmap-step">
            <div class="step-num">{step['step']}</div>
            <div class="step-body">
                <div class="step-phase">{step['phase']}</div>
                <div class="step-title">{step['title']}</div>
                <div class="step-desc">{step['desc']}</div>
                <div class="step-res">📚 <strong>Resources:</strong> {step['resources']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("---")
    st.success("🚀 Follow these steps consistently and you'll reach your goal. You've got this!")
    # Current skills display
    if skills:
        st.markdown('<div class="section-title" style="font-size:1rem; margin-top:8px;">Your Current Skills</div>', unsafe_allow_html=True)
        pills = "".join(f'<span class="tag-have">{s}</span>' for s in skills)
        st.markdown(f'<div class="tags" style="margin-top:10px;">{pills}</div>', unsafe_allow_html=True)
# ─────────────────────────────────────────────
# PAGE: ALL JOBS
# ─────────────────────────────────────────────
elif "All Jobs" in page:
    st.markdown("""
    <div class="hero-banner" style="padding:36px 40px;">
        <div class="hero-title" style="font-size:2rem;">📊 All Job Roles</div>
        <div class="hero-sub" style="font-size:0.95rem;">
            Browse all 15 roles in our database — skills required and salary ranges
        </div>
    </div>
    """, unsafe_allow_html=True)
    search = st.text_input("🔎 Search by job title or skill", placeholder="e.g. Python, React, Cloud...")
    filtered = JOB_KB
    if search.strip():
        q = search.strip().lower()
        filtered = [j for j in JOB_KB
                    if q in j["title"].lower()
                    or any(q in s.lower() for s in j["required_skills"])]
    st.markdown(f'<div class="section-sub">{len(filtered)} role(s) found</div>', unsafe_allow_html=True)
    for job in filtered:
        skill_pills = "".join(f'<span class="skill-pill">{s}</span>' for s in job["required_skills"])
        st.markdown(f"""
        <div class="job-card">
            <div class="job-title">{job['icon']}  {job['title']}</div>
            <div class="job-meta">
                🏢 {job['company_type']} &nbsp;·&nbsp;
                💰 <span>{job['salary']}</span>
            </div>
            <div class="job-desc">{job['description']}</div>
            <div class="job-skills">{skill_pills}</div>
        </div>
        """, unsafe_allow_html=True)
