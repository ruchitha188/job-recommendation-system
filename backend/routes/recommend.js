const express    = require('express');
const router     = express.Router();
const controller = require('../controllers/recommendController');

router.post('/', controller.getRecommendations);

module.exports = router;
