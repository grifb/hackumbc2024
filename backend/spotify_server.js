import express, { json, urlencoded } from 'express';
import cookieParser from 'cookie-parser';
import logger from 'morgan';
import indexRouter from './routes/index.js';
import 'dotenv/config';

const app = express();
const port = 3000;

app.use(logger('dev'));
app.use(json());
app.use(urlencoded({ extended: false }));
app.use(cookieParser());

app.use('/', indexRouter);

// This function will need to be called again when the 
// access token expires in about 1 hour
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

app.listen(port, () => {
    console.log(`App listening on port http://localhost:${port}`);
});
