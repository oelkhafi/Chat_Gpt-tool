import { Configuration, OpenAIApi } from "openai";
import { readFile, writeFile } from "fs/promises";
import { existsSync, mkdirSync } from "fs";
import { config } from "dotenv";
import fileNames from "./java_file_setup.mjs";


class gptTool {
    /**
     * @constructor
     * @param {string} apiKey -  api key for making api calls
     * @param {string[]} fileNames - array of file names to be processed
     */
    constructor(apiKey, fileNames) {
        try {
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
            // configure using .env file
            config();
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
            const response = await this.openai.createCompletion({
                model: "text-davinci-003",
                messages: [
                    // prompt to tell gpt what to do
                    { role: "system", content: `using this file of java code please answer the following user questions. here is the file: ${file}` },
                    // worth speration?
                    { role: "user", content: "yes or no: are the methods in this provided java class worth seperation?" },
                    // seperate, but we will only access if first response is yes
                    { role: "user", content: "separate the method in the following class code and only return the code, no explanation. be precise when identifying the java method in the java class" },
                    // suggest method names, but only access if first response is yes
                    { role: "user", content: "what would be the recommended method name for that seperated method?" },
                ],
                temperature: 0.2,
                max_tokens: 250,
                top_p: 1.0,
                frequency_penalty: 0.0,
                presence_penalty: 0.0,
            });
            // extracting responses from the response.data.choices object
            const responses = response.data.choices.map(choice => choice.message.content.trim());
            // return the responses
            return responses;
        } catch (error) {
            console.error("failed to prompt gpt for separation:", error);
            return [];
        }
    }

    /**
     * @function writeJavaFile
     * @description writes the contents of a java file to the "Refactor_Code" folder in the cwd
     * @param {string} fileContents - the contents of the java file
     * @param {string} fileName - the original file name in the format "java_code_#.java"
     * @returns {string} the new file name in the format "java_refact_#.java"
     */
    writeJavaFile(fileContents, fileName) {
        // extract file number
        const fileNumber = fileName.match(/\d+/)[0];
        // create the new file name
        const newFileName = `java_refact_${fileNumber}.java`;
        // write the file
        writeFile(newFileName, fileContents, (error) => {
            if (error) {
                console.error(`error writing file ${newFileName}: ${error}`);
            } else {
                console.log(`file ${newFileName} written successfully`);
            }
        });
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
                if (response === []) {
                    console.log(`api call error for ${this.fileNames[i]}, skipping`);
                    continue;
                }
                // check if the first response is "yes"
                const isFirstResponseYes = response[1].toLowerCase() === "yes";
                // if yes, assign responses of last two prompts to variables
                if (isFirstResponseYes) {
                    // extract the code and method name from the response
                    const separatedCode = response[2];
                    const methodName = response[3]; // <--- methodName is currently not in use - not sure how we plan to use
                    // write the new java file
                    const newFileName = this.writeJavaFile(separatedCode, this.fileNames[i]);
                    console.log(`code separated and saved to ${newFileName}`);
                } else {
                    console.log("seperation not suggested")
                }
            } catch (error) {
                console.error(`the following error occurred for file ${this.fileNames[i]} :`, error);
            }
        }
        // log success message to console
        console.log(`all ${this.fileNames.length} refactor(s) complete`);
    }
}

// create a new instance of the GptTool class
const gptTool = new gptTool(process.env.OPENAI_API_KEY, fileNames);
// refactor the files
gptTool.refactorFiles();


















// // prompt 1: Check if methods are worth separation
// const shouldSeparateMethods = await this.promptForSeparation(file);
// if (shouldSeparateMethods) {
//     // prompt 2: Separate the method in the following class code and only return the code
//     const refactoredCode = await this.promptForMethodRefactoring(file);
//     if (refactoredCode) {
//         // prompt 3: Recommend method names for the code segment
//         const recommendedMethodNames = await this.promptForMethodNames(file);
//         // perform further processing or actions based on the recommended method names
//         console.log(recommendedMethodNames);
//     }
// }