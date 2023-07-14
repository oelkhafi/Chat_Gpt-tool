import fs from 'fs';
import path from 'path';

// const sourceFolderPath = 'java_test_files/extra';
// const parentFolderPath = 'java_test_files';


// // MOVING AROUND JAVA TEST FILES //

// async function moveContents() {
//   try {
//     const files = await fs.readdir(sourceFolderPath);

//     for (const file of files) {
//       const sourcePath = path.join(sourceFolderPath, file);
//       const destinationPath = path.join(parentFolderPath, file);

//       await fs.rename(sourcePath, destinationPath);
//       console.log(`Moved ${sourcePath} to ${destinationPath}`);
//     }

//     console.log('All contents moved successfully!');
//   } catch (err) {
//     console.error('Failed to move contents:', err);
//   }
// }
// moveContents();



// // DELETE SUBFOLDER //

// await fs.rmdir(sourceFolderPath, { recursive: true });
// console.log(`Folder ${sourceFolderPath} and its contents deleted successfully!`);


// // RENAMING .JAVA FILES //

const folderPath = './Original_Code';
// const newFileName = 'java_code_';
// console.log("START")

// fs.readdir(folderPath, (err, files) => {
//     console.log("INSIDE")
//     if (err) {
//         console.error('Error reading folder:', err);
//         return;
//     }

//     const javaFiles = files.filter((file) => path.extname(file) === '.java');

//     const newNames = javaFiles.map((file, index) => {
//         const newName = `${newFileName}${index + 1}`;
//         const oldPath = path.join(folderPath, file);
//         const newPath = path.join(folderPath, newName);

//         fs.renameSync(oldPath, newPath);
//         return newName;
//     });

//     console.log('New file names:', newNames);
// });



// // ADDING .JAVA SUFFIX & GETTING RID OF .CLASS //

// fs.readdir(folderPath, (err, files) => {
//     if (err) {
//         console.error('Error reading folder:', err);
//         return;
//     }

//     files.forEach((file) => {
//         const filePath = path.join(folderPath, file);

//         if (path.extname(file) === '.class') {
//             // Delete files with .class extension
//             fs.unlinkSync(filePath);
//             console.log(`Deleted file: ${file}`);
//         } else {
//             // Rename files with different extensions
//             const newFile = `${file}.java`;
//             const newFilePath = path.join(folderPath, newFile);

//             fs.renameSync(filePath, newFilePath);
//             console.log(`Renamed file: ${file} to ${newFile}`);
//         }
//     });
// });



// // SAVING THE FILE NAMES TO AN ARRAY FOR LATER USE //

// const fileNames = [];

// fs.readdir(folderPath, (err, files) => {
//     if (err) {
//         console.error('Error reading folder:', err);
//         return;
//     }

//     files.forEach((file) => {
//         const fileName = path.basename(file);
//         fileNames.push(fileName);
//     });

//     console.log('File names:', fileNames);
// });

// export default fileNames;


// const fileNames = [];

// const files = fs.readdirSync(folderPath);
// files.forEach((file) => {
//     const fileName = path.basename(file);
//     fileNames.push(fileName);
// });

const files = fs.readdirSync(folderPath);
// const fileNames = files.map((file) => path.basename(file));
const fileNames = files
    .map((file) => {
        const fileName = path.basename(file);
        const numericPart = fileName.match(/\d+/); // Extract numerical part from file name
        return {
            fileName,
            numericPart: numericPart ? parseInt(numericPart[0]) : null // Convert to integer if numeric part exists
        };
    })
    .sort((a, b) => a.numericPart - b.numericPart)
    .map((file) => file.fileName);

// console.log('File names:', fileNames);

export default fileNames;