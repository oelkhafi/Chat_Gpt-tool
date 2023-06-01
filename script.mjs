// import { function } from "module" or "file"
import { appendFile } from "fs/promises";
import { readFile } from "fs/promises";
import { config } from "dotenv";
import { Configuration, OpenAIApi } from "openai";
import { writeFile } from "fs/promises";
import fileNames from "./splitFile.mjs";
// loading the environment variables from the .env file
config();

// creating new openai class instance & setting api key from .env
const openai = new OpenAIApi(
    new Configuration({
        apiKey: process.env.API_KEY,
    })
);
// defining async IIFE for local scope of variables & functions
(async () => {
    // for each element in fileNames array
    for (let i = 0; i < fileNames.length; i++) {
        // read file contents & construct url
        const file = await readFile(
            new URL(`Original_Code/${fileNames[i]}`, import.meta.url),
            "utf-8"
        );
        // send request to openai
        const res = await openai.createChatCompletion({
            model: "gpt-3.5-turbo",
            messages: [
                {
                    role: "user",
                    content: `refactor the following code - ${file} give only refactored code no explaination`,
                },
            ],
        });
        // extract refactored code from response
        const answer = res.data.choices[0].message.content.trim();
        // write refactored code to file
        await writeFile(`./Refactor_Code/refactor${i}.py`, `${answer}`);
        // log success message to console
        console.log("Data has been added to the file successfully.");
    }
})();