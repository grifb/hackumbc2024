import { Router } from 'express';
import { spawn } from 'child_process';
const router = Router();

/* GET home page. */
router.get('/', function(req, res, next) {
    res.end('Hello world!');
});

router.post('/download-video', async function(req, res, next) {
    if (!req.body.url)
    {
        res.status(400).end(`Url is missing!`);
    }

    const ytdlp = spawn('yt-dlp',
    [
        '-x',
        '--audio-format', 'wav',
        '-P', 'songs/',
        req.body.url
    ]);


    ytdlp.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
    });

    ytdlp.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });

    ytdlp.on('close', (code) => {
        console.log(`child process exited with code ${code}`);

        if (code == 0) { 
            res.end(`Queued up!`);
        } else {
            res.end(`An error occured while processing your video.`);
        }
    });

});


export default router;
