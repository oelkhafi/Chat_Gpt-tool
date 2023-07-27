// --------- STARTING GUIDE ---------
// run npm install to download dependencies
// run npm start to load the .env variables (api key)
// run npm refactor to run this script
// ----------------------------------

// import config from .env
import { config } from "dotenv";
config();
// package & module imports
import { Configuration, OpenAIApi } from "openai";
import { readFile, writeFile } from "fs/promises";
import { existsSync, mkdirSync, write } from "fs";
import fileNames from "./java_file_setup.mjs";



class gptTool {
    /**
     * @constructor
     * @param {string} apiKey -  api key for making api calls
     * @param {string[]} fileNames - array of file names to be processed
     */
    constructor(apiKey, fileNames) {
        console.log(apiKey)
        try {
            console.log(apiKey)
            this.fileNames = fileNames;
            // log success message to console
            console.log('file names setup complete');
        } catch (error) {
            // log error message to console
            console.error('file names setup failed: ', error);
        }
        try {
            // set directory paths for before & after files
            this.dir1 = "./Original_Code";
            this.dir2 = "./Refactor_Code";
            // check if directories exist & create them if not
            if (!existsSync(this.dir1)) {
                mkdirSync(this.dir1);
            } else if (!existsSync(this.dir2)) {
                mkdirSync(this.dir2);
            }
            // log success message to console
            console.log('directory setup complete');
        } catch (error) {
            // log error message to console
            console.error('directory setup failed: ', error);
        }
        try {
            // setup configuration (API key) for open ai calls
            this.configuration = new Configuration({
                apiKey: apiKey,
            });
            this.openai = new OpenAIApi(this.configuration);
            // log success message to console
            console.log('api congifuration complete');
        } catch (error) {
            // log error message to console
            console.error('api configuration failed: ', error);
        }
    }

    /**
     * @function readFileContents
     * @description reads the contents of a file contained in the "Original_Code" folder in the cwd
     * @param {string} fileName - the name of the file to read
     * @returns {Promise<string>} the contents of the file
     */
    async readFileContents(fileName) {
        try {
            // read file contents & construct url
            const file = await readFile(
                new URL(`Original_Code/${fileName}`, import.meta.url),
                "utf-8"
            );
            return file
        } catch (error) {
            console.error(`failed to read file ${fileName}:`, error);
            return "";
        }
    }

    /**
     * @function callGPT
     * @description calls the gpt api to ask questions about the provided java code
     * @param {string} file - the file of java code to use in the prompts
     * @returns {Promise<string[]>} the array of generated responses from the api
     */
    async callGPT(file) {
        try {
            // generate open ai completion
            const response = await this.openai.createCompletion({
                model: "text-davinci-003",
                prompt: `Evaluate the methods in the given Java class to determine if they require refactoring for separation. If separation is advised, provide the suggested code changes and recommended method names for the identified methods. Here is the class: ${file}`,
                temperature: 0, // randomness of response (1 = random, 0 = deterministic)
                max_tokens: 300, // max length of response
                top_p: 1.0, // probability of token selection - ignore
                frequency_penalty: 0.0, // likelihood of repeating (0 = reapeat responses, 1 = diverse responses)
                presence_penalty: 0.0, // adjust new responses/ideas (0 = trained content , 1 = original content)
            });
            // log response to console
            console.log(response.data.choices[0].text.trim());

            // extract refactored code from response
            // const answer = response.data.choices[0].message.content.trim();  <---- this doesnt work
            const answer = response.data.choices[0].text.trim();
            return answer;

        } catch (error) {
            console.error("failed to prompt gpt for separation:", error);
            return [];
        }
    }

    /**
     * @function writeJavaFile
     * @description writes the contents of a java file to the "Refactor_Code" folder in the cwd
     * @param {string} fileContents - the contents of the java file
     * @param {string} fileName - the original file name in the format "java_code_#.mjs"
     * @returns {string} the new file name in the format "java_refact_#.mjs"
     */
    async writeNewFile(fileContents, fileName) {
        // extract file number
        const fileNumber = fileName.match(/\d+/)[0];
        // create the new file name
        const newFileName = `java_refact_${fileNumber}.java`;
        // write the file
        const fileNPath = './Refactor_Code/' + newFileName;
        try {
            await writeFile(fileNPath, fileContents);
            console.log(`file ${newFileName} written successfully`);
        } catch {
            console.error(`error writing file ${newFileName}: ${error}`);
        }
        // return the new file name
        return newFileName;
    }

    /**
     * @function refactorFiles
     * @description refactors the files in the "Original_Code" folder & writes the refactored files to the "Refactor_Code" folder
     **/
    async refactorFiles() {
        // log the number of files to refactor
        console.log(`beginning refactor of ${this.fileNames.length} files`);
        // for each element in fileNames array
        for (let i = 0; i < this.fileNames.length; i++) {
            try {
                // log progress to console
                console.log(`refactoring file ${i + 1} of ${this.fileNames.length}`);
                // read file contents
                const file = await this.readFileContents(this.fileNames[i]);
                // check if file is empty
                if (file === "") {
                    console.log(`file ${this.fileNames[i]} is empty, skipping`);
                    continue;
                }

                // generate open ai completion
                const response = await this.callGPT(file);
                if (response.length === 0) {
                    console.log(`api call error for ${this.fileNames[i]}, skipping`);
                    continue;
                }

                // write the new java file
                const newFileName = this.writeNewFile(response, this.fileNames[i]);
                console.log(`code separated and saved to ${newFileName}`);

            } catch (error) {
                console.error(`the following error occurred for file ${this.fileNames[i]} :`, error);
            }
        }
        // log success message to console
        console.log(`all ${this.fileNames.length} refactor(s) complete`);
    }
}

// create a new instance of the GptTool class
const tool = new gptTool(process.env.API_KEY, fileNames);
// refactor the files
tool.refactorFiles();