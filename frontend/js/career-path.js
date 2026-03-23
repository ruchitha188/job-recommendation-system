// Renders the career roadmap from stored session data

window.addEventListener('load', () => {
  const profile   = JSON.parse(sessionStorage.getItem('userProfile') || 'null');
  const container = document.getElementById('careerSteps');

  if (!profile) return; // default message shown in HTML

  document.getElementById('pathSubtitle').textContent =
    `Career roadmap for ${profile.name} → ${profile.dreamJob}`;

  const roadmap = buildRoadmap(profile.skills || [], profile.dreamJob);

  container.innerHTML = roadmap.map((step, i) => `
    <div class="step">
      <div class="step-number">${i + 1}</div>
      <div class="step-content">
        <h3>${step.title}</h3>
        <p>${step.description}</p>
        ${step.resources
          ? `<p style="margin-top:8px;"><strong>📚 Resources:</strong> ${step.resources}</p>`
          : ''}
      </div>
    </div>`).join('');
});

function buildRoadmap(skills, dreamJob) {
  const d = dreamJob.toLowerCase();

  return [
    {
      title: '📚 Strengthen Fundamentals',
      description: `Build a solid base in Data Structures, Algorithms, and ${pickLang(d)}.
                    These underpin every technical role.`,
      resources: 'CS50 (Harvard), GeeksforGeeks, Codecademy'
    },
    {
      title: `🎯 Learn Core Skills for "${dreamJob}"`,
      description: coreDesc(d),
      resources: coreRes(d)
    },
    {
      title: '🛠️ Build 2–3 Portfolio Projects',
      description: 'Create real projects that demonstrate your skills. Host them on GitHub and deploy at least one live project.',
      resources: 'GitHub, Vercel (frontend), Render (backend), AWS Free Tier'
    },
    {
      title: '📖 Advanced Specialisation',
      description: advDesc(d),
      resources: advRes(d)
    },
    {
      title: '🏆 Certifications & Practice',
      description: 'Earn recognised certifications in your domain and practice problem-solving on competitive platforms.',
      resources: certs(d)
    },
    {
      title: '🤝 Build Your Network & Apply',
      description: 'Update LinkedIn, write a targeted resume, and apply consistently. Aim for 5–10 applications per week.',
      resources: 'LinkedIn, Naukri, Internshala, Wellfound'
    },
    {
      title: '🚀 Interview Prep & Land the Job',
      description: 'Practice DSA, system design, and role-specific questions. Do mock interviews to build confidence.',
      resources: 'LeetCode, HackerRank, Pramp, InterviewBit'
    }
  ];
}

function pickLang(d) {
  if (d.includes('web') || d.includes('frontend')) return 'JavaScript';
  if (d.includes('data') || d.includes('ai') || d.includes('ml')) return 'Python';
  return 'Python or Java';
}
function coreDesc(d) {
  if (d.includes('ai') || d.includes('ml')) return 'Focus on Python, NumPy, Pandas, scikit-learn, and intro Deep Learning with TensorFlow or PyTorch.';
  if (d.includes('data')) return 'Master Python, R, SQL, statistics, data wrangling, and visualisation with Matplotlib and Tableau.';
  if (d.includes('web') || d.includes('full')) return 'Learn HTML, CSS, JavaScript deeply. Then React for frontend and Node.js + Express for backend.';
  return `Study the core tools and languages used by professionals in the ${d} field.`;
}
function coreRes(d) {
  if (d.includes('ai') || d.includes('ml') || d.includes('data')) return 'Kaggle Learn, fast.ai, Andrew Ng ML Course (Coursera)';
  if (d.includes('web') || d.includes('full')) return 'The Odin Project, freeCodeCamp, MDN Web Docs';
  return 'Coursera, edX, Udemy, official documentation';
}
function advDesc(d) {
  if (d.includes('ai') || d.includes('ml')) return 'Dive into NLP, Computer Vision, Transformers, and MLOps — model deployment with FastAPI and Docker.';
  if (d.includes('data')) return 'Learn Big Data tools (Spark), advanced SQL, and cloud data warehouses like BigQuery or Snowflake.';
  if (d.includes('web') || d.includes('full')) return 'Master TypeScript, Next.js, GraphQL, microservices, Docker, and Kubernetes.';
  return 'Specialise in cutting-edge tools relevant to your chosen role.';
}
function advRes(d) {
  if (d.includes('ai') || d.includes('ml') || d.includes('data')) return 'Papers With Code, Hugging Face, Full Stack Deep Learning, MLflow docs';
  return 'Official docs, GitHub trending, Medium, Dev.to';
}
function certs(d) {
  if (d.includes('ai') || d.includes('ml') || d.includes('data')) return 'Google ML Engineer Cert, TensorFlow Developer Cert, IBM Data Science (Coursera)';
  if (d.includes('cloud') || d.includes('devops')) return 'AWS Solutions Architect, Google ACE, CKA (Kubernetes), HashiCorp Terraform';
  return 'freeCodeCamp certifications, Meta Developer certificates, LeetCode for practice';
}
