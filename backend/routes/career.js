const express    = require('express');
const router     = express.Router();
const controller = require('../controllers/careerController');

router.post('/', controller.getCareerPath);

module.exports = router;
