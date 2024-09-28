import { Router } from 'express';
const router = Router();

async function getAccessToken() {
  // https://developer.spotify.com/documentation/web-api/tutorials/client-credentials-flow
  const response = await fetch(`https://accounts.spotify.com/api/token`, {
      body: new URLSearchParams({
          'grant_type': 'client_credentials'
      }),
      method: `POST`,
      headers: {
          'Authorization': 'Basic ' + (new Buffer.from(process.env.SPOTIFY_CLIENT_ID + ':' + process.env.SPOTIFY_CLIENT_SECRET).toString('base64')),
          'Content-Type': 'application/x-www-form-urlencoded'
      }
  });
  const parsed = await response.json();
  return parsed["access_token"];
}

let accessToken = getAccessToken();
/* GET home page. */
router.get('/', function(req, res, next) {
    res.end('Hello world!');
});

router.get('/me',async function(req,res,next) {
  const r = await fetch(`https://api.spotify.com/v1/me`,{
  headers: {
    'Authorization': `Bearer: ${accessToken}` 
  }
})
const data = await r.json();
res.end(data.email);
});


export default router;
