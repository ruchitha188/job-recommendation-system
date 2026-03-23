require('dotenv').config();
const express = require('express');
const cors    = require('cors');

const recommendRoutes = require('./routes/recommend');
const careerRoutes    = require('./routes/career');
const userRoutes      = require('./routes/user');

const app  = express();
const PORT = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

// Health check
app.get('/', (req, res) => {
  res.json({ message: 'Job Recommendation API is running ✅' });
});

app.use('/api/recommend', recommendRoutes);
app.use('/api/career',    careerRoutes);
app.use('/api/users',     userRoutes);

// Global error handler
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
});

app.listen(PORT, () => {
  console.log(`🚀 Server running on http://localhost:${PORT}`);
});
