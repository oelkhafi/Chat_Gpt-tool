// automate the process of setting up the environment variables
// this script will run every time npm start is run
// and will load .env variables since can't do that in mjs files
// @ drew carranti
import { config } from 'dotenv';

config();

console.log('API Key:', process.env.API_KEY);