import express, { json, urlencoded } from 'express';
import cookieParser from 'cookie-parser';
import logger from 'morgan';
import cors from 'cors';
import indexRouter from './routes/index.js';
import 'dotenv/config';

const app = express();
const port = 3000;

app.use(logger('dev'));
app.use(json());
app.use(urlencoded({ extended: false }));
app.use(cookieParser());
app.use(cors());

app.use('/', indexRouter);

app.listen(port, () => {
    console.log(`App listening on port http://localhost:${port}`);
});
