// TODO: check responses & make appropriate adjustments - drew carranti - 6/6/23

// import libraries & external variables
import { Configuration, OpenAIApi } from "openai";
import { readFile, writeFile } from "fs/promises";
import { config } from "dotenv";
import { existsSync, mkdirSync } from "fs";
import fileNames from "./java_file_setup.mjs";


// configure using .env file
config();
// setup configuration (API key) for open ai calls
const configuration = new Configuration({
    apiKey: process.env.API_KEY,
});
const openai = new OpenAIApi(configuration);
// log success message to console
console.log('successful api configuration');



// set directory paths for before & after files
const dir1 = './Original_Code';
const dir2 = './Refactor_Code';
// checking if directories exist & creating if not
if (!existsSync(dir1)) {
    mkdirSync(dir1);
} else if (!existsSync(dir2)) {
    mkdirSync(dir2);
}
// log success message to console
console.log('successful directory setup');


// identify number of files to refactor
const length = fileNames.length;
console.log(`beginning refactor of ${length} files`);

// defining async IIFE for local scope of variables & functions
(async () => {
    // for each element in fileNames array
    for (let i = 0; i < length; i++) {
        // log progress to console
        console.log(`refactoring file ${i} of ${length}`);

        // read file contents & construct url
        const file = await readFile(
            new URL(`Original_Code/${fileNames[i]}`, import.meta.url),
            "utf-8"
        );

        // generate open ai completion
        const response = await openai.createCompletion({
            model: "text-davinci-003",
            prompt: `REFACTOR THE METHOD IN THE FOLLOWING CLASS CODE AND ONLY RETURN THE CODE, NO EXPLANATION. BE PRECISE WHEN IDENTIFYING THE JAVA METHOD IN THE JAVA CLASS: ${file}`,
            temperature: 0, // randomness of response (1 = random, 0 = deterministic)
            max_tokens: 64, // max length of response
            top_p: 1.0, // probability of token selection - ignore
            frequency_penalty: 0.0, // likelihood of repeating (0 = reapeat responses, 1 = diverse responses)
            presence_penalty: 0.0, // adjust new responses/ideas (0 = trained content , 1 = original content)
        });
        // log response to console
        // console.log(response.data.choices[0].text);

        // extract refactored code from response
        // const answer = response.data.choices[0].message.content.trim();  <---- this doesnt work
        const answer = response.data.choices[0].text.trim();

        // write refactored code to file
        await writeFile(`./Refactor_Code/java_refactored_${i + 1}.java`, `${answer}`);
        // log success message to console
        // console.log(`${fileNames[i]} refactored successfully - exported as java_refactored_${i + 1}.java`);
    }
})();


















// // * * * TESTING * * * //
// const fileT = await readFile(
//     new URL(`Original_Code/${fileNames[0]}`, import.meta.url),
//     "utf-8"
// );
// console.log("FILE:", fileT);
// try {
//     // generate open ai completion
//     const response = await openai.createCompletion({
//         model: "text-davinci-003",
//         prompt: `refactor the method within the class in the following code - ${fileT} give only the refactored method, no explaination`,
//         temperature: 0, // randomness of response (1 = random, 0 = deterministic)
//         max_tokens: 64, // max length of response
//         top_p: 1.0, // probability of token selection - ignore
//         frequency_penalty: 0.0, // likelihood of repeating (0 = reapeat responses, 1 = diverse responses)
//         presence_penalty: 0.0, // adjust new responses/ideas (0 = trained content , 1 = original content)
//     });
//     // extract refactored code from response
//     console.log("ALL: ", response.data.choices[0]);
//     console.log("TEXT: ", response.data.choices[0].text);

// } catch (error) {
//     if (error.response) {
//         console.log("error:", error.response.status);
//         console.log("error response:", error.response.data);
//     } else {
//         console.log("error message:", error.message);
//     }
// }