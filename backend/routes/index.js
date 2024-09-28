import { Router } from 'express';
const router = Router();

/* GET home page. */
router.get('/', function(req, res, next) {
    res.end('Hello world!');
});

export default router;
