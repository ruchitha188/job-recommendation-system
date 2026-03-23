-- Run this once to set up the entire database
CREATE DATABASE IF NOT EXISTS job_recommendation_db;
USE job_recommendation_db;

-- Users table
CREATE TABLE IF NOT EXISTS users (
  id          INT AUTO_INCREMENT PRIMARY KEY,
  name        VARCHAR(100) NOT NULL,
  skills      TEXT NOT NULL,
  dream_job   VARCHAR(100),
  experience  INT DEFAULT 0,
  created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Jobs table
CREATE TABLE IF NOT EXISTS jobs (
  id              INT AUTO_INCREMENT PRIMARY KEY,
  title           VARCHAR(100) NOT NULL,
  company_type    VARCHAR(100),
  salary          VARCHAR(100),
  required_skills TEXT,
  description     TEXT,
  created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Recommendations table
CREATE TABLE IF NOT EXISTS recommendations (
  id          INT AUTO_INCREMENT PRIMARY KEY,
  user_id     INT NOT NULL,
  job_id      INT NOT NULL,
  match_score INT,
  created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (job_id)  REFERENCES jobs(id)
);

-- Seed 10 sample jobs
INSERT INTO jobs (title, company_type, salary, required_skills, description) VALUES
('AI Engineer',
 'Tech / Product', '₹12–25 LPA',
 '["Python","TensorFlow","PyTorch","Machine Learning","Docker","AWS"]',
 'Design, build, and deploy AI/ML models into production systems.'),
('Data Scientist',
 'Analytics / Consulting', '₹8–18 LPA',
 '["Python","R","SQL","Statistics","Pandas","Tableau"]',
 'Analyse large datasets to extract insights and build predictive models.'),
('Machine Learning Engineer',
 'Startup / Enterprise', '₹10–20 LPA',
 '["Python","scikit-learn","Spark","SQL","Docker"]',
 'Build and maintain ML pipelines and model training infrastructure.'),
('Full Stack Developer',
 'Product / Service', '₹6–16 LPA',
 '["HTML","CSS","JavaScript","Node.js","React","MySQL"]',
 'Develop end-to-end web applications covering frontend and backend.'),
('Frontend Developer',
 'Agency / Product', '₹4–12 LPA',
 '["HTML","CSS","JavaScript","React","TypeScript"]',
 'Build responsive and accessible user interfaces.'),
('Backend Developer',
 'Enterprise / Startup', '₹5–14 LPA',
 '["Node.js","Python","SQL","REST API","Docker"]',
 'Design APIs, databases, and server-side application logic.'),
('Data Analyst',
 'Finance / E-commerce', '₹4–10 LPA',
 '["SQL","Excel","Python","Tableau","Power BI"]',
 'Transform raw data into actionable business insights.'),
('DevOps Engineer',
 'Enterprise / Cloud', '₹8–20 LPA',
 '["Linux","Docker","Kubernetes","Jenkins","AWS","Terraform"]',
 'Automate CI/CD pipelines and manage cloud infrastructure.'),
('Cloud Engineer',
 'IT / Consulting', '₹8–18 LPA',
 '["AWS","Azure","GCP","Terraform","Linux","Python"]',
 'Architect and maintain cloud-based infrastructure and services.'),
('Cybersecurity Analyst',
 'Finance / Government', '₹6–15 LPA',
 '["Networking","Linux","Python","Ethical Hacking","SIEM"]',
 'Protect systems and data from cyber threats.');
