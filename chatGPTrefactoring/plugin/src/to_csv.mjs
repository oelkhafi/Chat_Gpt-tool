import fileNames from "../../../nodejs_project/java_file_setup.mjs";
import fs from 'fs';

// Convert array to CSV string
const csvString = fileNames.join(',');

// Write CSV string to a file
fs.writeFileSync('fileNames.csv', csvString);
