// import { function } from "module" or "file"
import { existsSync, mkdirSync, writeFile } from "fs";
import { readFile } from "fs/promises";
// read file & construct url 
const file = await readFile(
  new URL("beforeFinal.csv", import.meta.url),
  "utf-8"
);
// set directory paths for before & after files
const dir1 = '../Original_Code';
const dir2 = '../Refactor_Code';
// checking if directories exist & creating if not
if (!existsSync(dir1) || !existsSync(dir2)) {
  mkdirSync(dir1);
  mkdirSync(dir2);

}
// spliting file based on specified delimiter
const fileData = file.split(`-End,"\n `);
// log number of files read
console.log(`Total number of files read: ${fileData.length}`);
// creating empty array for filenames & intiialize counter
const fileNames = [];
let counter = 0;
// loop through fileData array, check length & write contents to original code file
for (let i = 1; i < fileData.length; i++) {
  if (fileData[i].split("\n").length > 20) {
    await writeFile(`./Original_Code/code${i}.py`, `${fileData[i]}`, (err) => {
      if (err) throw err;
    });
    // add file name to fileNames array & increment
    fileNames.push(`code${i}.py`);
    counter++;
  }
}
// log value of counter, fileNames, & export fileNames array as default export of the module
console.log(counter);
console.log(fileNames);
export default fileNames;

