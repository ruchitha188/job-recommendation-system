const db = require('../config/db');

exports.saveUser = async (req, res) => {
  const { name, skills, dreamJob, experience } = req.body;
  if (!name || !skills) {
    return res.status(400).json({ error: 'name and skills are required' });
  }
  try {
    const [result] = await db.query(
      'INSERT INTO users (name, skills, dream_job, experience) VALUES (?, ?, ?, ?)',
      [name, JSON.stringify(skills), dreamJob, experience || 0]
    );
    res.json({ id: result.insertId, message: 'User saved successfully' });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Failed to save user' });
  }
};

exports.getUser = async (req, res) => {
  try {
    const [rows] = await db.query('SELECT * FROM users WHERE id = ?', [req.params.id]);
    if (!rows.length) return res.status(404).json({ error: 'User not found' });
    const user = rows[0];
    user.skills = JSON.parse(user.skills || '[]');
    res.json(user);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Failed to fetch user' });
  }
};
```

---

## ✅ Final Checklist — Total Files Per Folder

| Folder | Files to create |
|---|---|
| `job-recommendation-system/` (root) | `.gitignore`, `README.md` |
| `frontend/` | `index.html` |
| `frontend/css/` | `style.css` |
| `frontend/js/` | `main.js`, `recommend.js`, `career-path.js` |
| `frontend/pages/` | `recommend.html`, `career-path.html` |
| `database/` | `schema.sql` |
| `backend/` | `server.js`, `package.json`, `.env.example` |
| `backend/config/` | `db.js` |
| `backend/routes/` | `recommend.js`, `career.js`, `user.js` |
| `backend/controllers/` | `recommendController.js`, `careerController.js`, `userController.js` |

**9 folders, 20 files total.** Once all are created, run:
```
cd backend
npm install
npm run dev
