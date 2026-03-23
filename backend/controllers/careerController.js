const ROADMAPS = {
  'ai engineer': [
    { phase: 'Basics',      title: 'Python & Math Foundations',
      desc: 'Learn Python, NumPy, Pandas. Study Linear Algebra and Statistics.',
      resources: 'CS50P, Khan Academy, Real Python' },
    { phase: 'Core',        title: 'Machine Learning Fundamentals',
      desc: 'Supervised/unsupervised learning, model evaluation, scikit-learn.',
      resources: 'Andrew Ng ML Course (Coursera), Kaggle Learn' },
    { phase: 'Advanced',    title: 'Deep Learning & Frameworks',
      desc: 'TensorFlow, PyTorch, CNNs, RNNs, Transformers, and NLP.',
      resources: 'fast.ai, Deep Learning Specialisation, Hugging Face' },
    { phase: 'Projects',    title: 'Portfolio Projects',
      desc: 'Build image classifier, chatbot, recommendation engine. Deploy with FastAPI.',
      resources: 'GitHub, Render, AWS EC2' },
    { phase: 'Apply',       title: 'Certifications & Apply',
      desc: 'Google ML Engineer or TensorFlow Developer cert. Apply on LinkedIn/Naukri.',
      resources: 'LeetCode, Pramp, LinkedIn, Naukri' }
  ],
  'data scientist': [
    { phase: 'Basics',  title: 'Python & Statistics',
      desc: 'Python, Pandas, NumPy. Descriptive statistics and hypothesis testing.',
      resources: 'Codecademy, StatQuest (YouTube)' },
    { phase: 'Core',    title: 'Data Wrangling & Visualisation',
      desc: 'Data cleaning, Matplotlib, Seaborn, Tableau, Power BI.',
      resources: 'Kaggle, Tableau Public' },
    { phase: 'Advanced',title: 'ML & Big Data',
      desc: 'Apply ML models, advanced SQL, Spark, cloud data warehouses.',
      resources: 'Coursera Data Science Specialisation' },
    { phase: 'Apply',   title: 'Certifications & Apply',
      desc: 'IBM Data Science or Google Data Analytics certificate.',
      resources: 'Coursera, LinkedIn, Naukri, Wellfound' }
  ],
  'full stack developer': [
    { phase: 'Basics',  title: 'HTML, CSS & JavaScript',
      desc: 'Semantic HTML, CSS Flexbox/Grid, core JavaScript ES6+.',
      resources: 'freeCodeCamp, The Odin Project, MDN Web Docs' },
    { phase: 'Core',    title: 'React & Node.js',
      desc: 'Frontend with React, backend APIs with Node.js + Express.',
      resources: 'React docs, Express docs' },
    { phase: 'Database',title: 'MySQL & MongoDB',
      desc: 'Relational DB design with MySQL and NoSQL with MongoDB.',
      resources: 'MySQL Tutorial, MongoDB University' },
    { phase: 'Projects',title: 'Full Stack Apps',
      desc: 'Build 2 full-stack apps. Deploy on Vercel + Render.',
      resources: 'GitHub, Vercel, Render' },
    { phase: 'Apply',   title: 'Apply & Interview Prep',
      desc: 'Practice system design and LeetCode. Apply on LinkedIn, Naukri.',
      resources: 'LeetCode, system-design-primer (GitHub)' }
  ]
};

function matchRoadmap(dreamJob) {
  const d = dreamJob.toLowerCase();
  for (const key of Object.keys(ROADMAPS)) {
    if (d.includes(key) || key.split(' ').every(w => d.includes(w))) {
      return ROADMAPS[key];
    }
  }
  // Generic fallback
  return [
    { phase: 'Basics',   title: 'Core Programming Fundamentals',
      desc: `Learn programming basics relevant to ${dreamJob}.`,
      resources: 'CS50 (Harvard), freeCodeCamp, GeeksforGeeks' },
    { phase: 'Core',     title: `Domain Skills for ${dreamJob}`,
      desc: 'Research and build proficiency in the key tools of your target role.',
      resources: 'Coursera, Udemy, official documentation' },
    { phase: 'Projects', title: 'Build Portfolio Projects',
      desc: 'Create 2–3 real projects. Host on GitHub.',
      resources: 'GitHub, Vercel, Render' },
    { phase: 'Apply',    title: 'Certifications & Apply',
      desc: 'Earn certifications and start applying for roles.',
      resources: 'LinkedIn, Naukri, LeetCode, Pramp' }
  ];
}

exports.getCareerPath = (req, res) => {
  const { dreamJob } = req.body;
  if (!dreamJob) return res.status(400).json({ error: 'dreamJob is required' });
  const steps = matchRoadmap(dreamJob);
  res.json({ dreamJob, steps });
};
