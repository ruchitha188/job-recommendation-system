const db = require('../config/db');

// Job knowledge base (fallback when DB is empty)
const JOB_KB = [
  { title: 'AI Engineer', companyType: 'Tech / Product', salary: '₹12–25 LPA',
    requiredSkills: ['Python','TensorFlow','PyTorch','Machine Learning','Docker','AWS'],
    description: 'Design, build, and deploy AI/ML models into production.' },
  { title: 'Data Scientist', companyType: 'Analytics', salary: '₹8–18 LPA',
    requiredSkills: ['Python','R','SQL','Statistics','Pandas','Tableau'],
    description: 'Analyse data and build predictive models.' },
  { title: 'ML Engineer', companyType: 'Startup', salary: '₹10–20 LPA',
    requiredSkills: ['Python','scikit-learn','Spark','SQL','Docker'],
    description: 'Build and maintain ML pipelines.' },
  { title: 'Full Stack Developer', companyType: 'Product', salary: '₹6–16 LPA',
    requiredSkills: ['HTML','CSS','JavaScript','Node.js','React','MySQL'],
    description: 'Develop complete web applications.' },
  { title: 'Data Analyst', companyType: 'Finance', salary: '₹4–10 LPA',
    requiredSkills: ['SQL','Excel','Python','Tableau','Power BI'],
    description: 'Turn raw data into business insights.' },
  { title: 'DevOps Engineer', companyType: 'Enterprise', salary: '₹8–20 LPA',
    requiredSkills: ['Linux','Docker','Kubernetes','Jenkins','AWS'],
    description: 'Automate pipelines and manage cloud infra.' },
];

function calcScore(userSkills, requiredSkills) {
  const user = userSkills.map(s => s.toLowerCase());
  const req  = requiredSkills.map(s => s.toLowerCase());
  if (!req.length) return 0;
  const matched = req.filter(r => user.some(u => u.includes(r) || r.includes(u)));
  return Math.round((matched.length / req.length) * 100);
}

exports.getRecommendations = async (req, res) => {
  const { name, skills, experience, dreamJob } = req.body;

  if (!skills || !Array.isArray(skills) || skills.length === 0) {
    return res.status(400).json({ error: 'skills array is required' });
  }

  try {
    let jobs = [];
    try {
      const [rows] = await db.query('SELECT * FROM jobs');
      if (rows.length > 0) {
        jobs = rows.map(r => ({
          ...r,
          requiredSkills: JSON.parse(r.required_skills || '[]')
        }));
      }
    } catch (_) {
      jobs = JOB_KB; // fallback to knowledge base
    }

    const scored = jobs
      .map(job => ({ ...job, matchScore: calcScore(skills, job.requiredSkills) }))
      .filter(job => job.matchScore > 0)
      .sort((a, b) => b.matchScore - a.matchScore)
      .slice(0, 6);

    // Save user (best-effort)
    try {
      await db.query(
        'INSERT INTO users (name, skills, dream_job, experience) VALUES (?, ?, ?, ?)',
        [name, JSON.stringify(skills), dreamJob, experience || 0]
      );
    } catch (_) {}

    res.json({ jobs: scored });

  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Internal server error' });
  }
};
