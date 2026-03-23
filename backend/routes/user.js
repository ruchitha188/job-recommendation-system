const express    = require('express');
const router     = express.Router();
const controller = require('../controllers/userController');

router.post('/',    controller.saveUser);
router.get('/:id',  controller.getUser);

module.exports = router;
