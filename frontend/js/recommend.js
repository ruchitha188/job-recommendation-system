// Handles the recommendation form, API call, and result rendering

async function getRecommendations() {
  const name     = document.getElementById('name').value.trim();
  const skills   = document.getElementById('skills').value.trim();
  const exp      = document.getElementById('experience').value;
  const dreamJob = document.getElementById('dreamJob').value.trim();
  const interests= document.getElementById('interests').value.trim();
  const errorDiv = document.getElementById('errorMsg');

  errorDiv.textContent = '';

  if (!name || !skills || !dreamJob) {
    errorDiv.textContent = 'Please fill in Name, Skills, and Dream Job.';
    return;
  }

  const btn = document.querySelector('.btn-submit');
  btn.textContent = '⏳ Analyzing...';
  btn.disabled = true;

  try {
    const res = await fetch('http://localhost:5000/api/recommend', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name,
        skills: parseSkills(skills),
        experience: parseInt(exp),
        dreamJob,
        interests
      })
    });

    if (!res.ok) throw new Error('Server error');
    const data = await res.json();

    sessionStorage.setItem('userProfile', JSON.stringify({ name, skills: parseSkills(skills), dreamJob }));
    sessionStorage.setItem('recommendations', JSON.stringify(data));
    renderResults(data, parseSkills(skills));

  } catch (err) {
    // Demo mode when backend is not running
    const demo = demoData(parseSkills(skills), dreamJob);
    sessionStorage.setItem('userProfile', JSON.stringify({ name, skills: parseSkills(skills), dreamJob }));
    renderResults(demo, parseSkills(skills));
  }

  btn.textContent = '🔍 Get Recommendations';
  btn.disabled = false;
}

function renderResults(data, userSkills) {
  document.getElementById('resultsSection').style.display = 'block';

  const allRequired = [...new Set(data.jobs.flatMap(j => j.requiredSkills || []))];
  const have    = userSkills.filter(s =>
    allRequired.map(x => x.toLowerCase()).includes(s.toLowerCase())
  );
  const missing = allRequired.filter(s =>
    !userSkills.map(x => x.toLowerCase()).includes(s.toLowerCase())
  );

  document.getElementById('gapAnalysis').innerHTML = `
    <div class="gap-box have">
      <h3>✅ Skills You Have</h3>
      ${(have.length ? have : userSkills).map(s => `<span class="skill-tag">${s}</span>`).join('')}
    </div>
    <div class="gap-box missing">
      <h3>⚠️ Skills to Acquire</h3>
      ${missing.length
        ? missing.map(s => `<span class="skill-tag">${s}</span>`).join('')
        : '<span class="skill-tag">Great match — no major gaps!</span>'}
    </div>`;

  document.getElementById('jobResults').innerHTML = data.jobs.map(job => `
    <div class="result-card">
      <span class="match-score">${job.matchScore}% Match</span>
      <h3>${job.title}</h3>
      <p><strong>Company Type:</strong> ${job.companyType} &nbsp;|&nbsp;
         <strong>Salary:</strong> ${job.salary}</p>
      <p style="margin-top:8px;">${job.description}</p>
      <p style="margin-top:8px;"><em>Required Skills:</em>
         ${(job.requiredSkills || []).join(', ')}</p>
    </div>`).join('');

  document.getElementById('resultsSection').scrollIntoView({ behavior: 'smooth' });
}

// Demo data used when backend is offline
function demoData(skills, dreamJob) {
  const d = dreamJob.toLowerCase();
  const jobs = [
    {
      title: d.includes('ai') || d.includes('ml') ? 'AI Engineer' : 'Full Stack Developer',
      companyType: 'Tech / Product',
      salary: '₹12–25 LPA',
      matchScore: 88,
      description: 'Build and deploy intelligent systems in production environments.',
      requiredSkills: ['Python', 'TensorFlow', 'Docker', 'AWS', 'SQL']
    },
    {
      title: 'Data Scientist',
      companyType: 'Analytics / Consulting',
      salary: '₹8–18 LPA',
      matchScore: 74,
      description: 'Analyse large datasets and build predictive models.',
      requiredSkills: ['Python', 'R', 'SQL', 'Statistics', 'Tableau']
    },
    {
      title: 'ML Engineer',
      companyType: 'Startup / Enterprise',
      salary: '₹10–20 LPA',
      matchScore: 65,
      description: 'Design ML pipelines and maintain training infrastructure.',
      requiredSkills: ['Python', 'scikit-learn', 'Spark', 'Docker']
    }
  ];
  return { jobs };
}
