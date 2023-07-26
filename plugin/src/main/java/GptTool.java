package tool.gpt;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

import com.theokanning.openai.completion.CompletionRequest;
import com.theokanning.openai.completion.OpenAICompletionResponse;

public class GptTool {
    private List<String> fileNames;
    private String dir1;
    private String dir2;
    private Configuration configuration;
    private OpenAIApi openai;

    /**
     * Constructor for GptTool class.
     */
    public GptTool() {
        try {
            this.fileNames = FileNames.getFileNames();
            // log success message to console
            System.out.println("File names setup complete");
        } catch (Exception e) {
            // log error message to console
            System.err.println("File names setup failed: " + e.getMessage());
        }

        try {
            // set directory paths for before & after files
            this.dir1 = "../resources/code_files/Original_Code";
            this.dir2 = "../resources/code_files/Refactor_Code";
            // check if directories exist & create them if not
            createDirectoryIfNeeded(dir1);
            createDirectoryIfNeeded(dir2);
            // log success message to console
            System.out.println("Directory setup complete");
        } catch (Exception e) {
            // log error message to console
            System.err.println("Directory setup failed: " + e.getMessage());
        }

        try {
            // setup configuration (API key) for open ai calls
            this.configuration = new Configuration();
            this.configuration.setApiKey(API_KEY);
            this.openai = new OpenAIApi(configuration);
            // log success message to console
            System.out.println("API configuration complete");
        } catch (Exception e) {
            // log error message to console
            System.err.println("API configuration failed: " + e.getMessage());
        }
    }

    /**
     * Reads the contents of a file.
     *
     * @param fileName the name of the file to read.
     * @return the contents of the file.
     */
    public String readFileContents(String fileName) {
        try {
            // read file contents & construct path
            String filePath = "../resources/code_files/Original_Code/" + fileName;
            byte[] fileBytes = Files.readAllBytes(Path.of(filePath));
            return new String(fileBytes);
        } catch (IOException e) {
            System.err.println("Failed to read file " + fileName + ": " + e.getMessage());
            return "";
        }
    }

    /**
     * Calls the GPT API to ask questions about the provided Java code.
     *
     * @param file the Java code file to use in the prompts.
     * @return the array of generated responses from the API.
     */
    public List<String> callGPT(String file) {
        try {
            // generate open ai completion
            String prompt = "Evaluate the methods in the given Java class to determine if they require refactoring for separation. If separation is advised, provide the suggested code changes and recommended method names for the identified methods. Here is the class: " + file;
            CompletionRequest completionRequest = new CompletionRequest.Builder()
                    .model("text-davinci-003")
                    .prompt(prompt)
                    .temperature(0) // randomness of response (1 = random, 0 = deterministic)
                    .maxTokens(300) // max length of response
                    .topP(1.0) // probability of token selection - ignore
                    .frequencyPenalty(0.0) // likelihood of repeating (0 = repeat responses, 1 = diverse responses)
                    .presencePenalty(0.0) // adjust new responses/ideas (0 = trained content, 1 = original content)
                    .build();
            OpenAICompletionResponse completionResponse = openai.createCompletion(completionRequest);
            // log response to console
            System.out.println(completionResponse.getChoices().get(0).getText().trim());
            // extract refactored code from response
            String answer = completionResponse.getChoices().get(0).getText().trim();
            List<String> response = new ArrayList<>();
            response.add(answer);
            return response;
        } catch (Exception e) {
            System.err.println("Failed to prompt GPT for separation: " + e.getMessage());
            return new ArrayList<>();
        }
    }

    /**
     * Writes the contents of a Java file.
     *
     * @param fileContents the contents of the Java file.
     * @param fileName     the original file name.
     */
    public void writeNewFile(String fileContents, String fileName) {
        // extract file number
        String fileNumber = fileName.replaceAll("[^\\d.]", "");
        // create the new file name
        String newFileName = "java_refact_" + fileNumber + ".java";
        // write the file
        String filePath = "../resources/code_files/Refactor_Code/" + newFileName;
        try {
            Files.writeString(Path.of(filePath), fileContents);
            System.out.println("File " + newFileName + " written successfully");
        } catch (IOException e) {
            System.err.println("Error writing file " + newFileName + ": " + e.getMessage());
        }
    }

    /**
     * Refactors the files in the "Original_Code" folder and writes the refactored files to the "Refactor_Code" folder.
     */
    public void refactorFiles() {
        // log the number of files to refactor
        System.out.println("Beginning refactor of " + fileNames.size() + " files");
        // for each element in fileNames array
        for (int i = 0; i < fileNames.size(); i++) {
            try {
                // log progress to console
                System.out.println("Refactoring file " + (i + 1) + " of " + fileNames.size());
                // read file contents
                String file = readFileContents(fileNames.get(i));
                // check if file is empty
                if (file.isEmpty()) {
                    System.out.println("File " + fileNames.get(i) + " is empty, skipping");
                    continue;
                }
                // generate open ai completion
                List<String> response = callGPT(file);
                if (response.isEmpty()) {
                    System.out.println("API call error for " + fileNames.get(i) + ", skipping");
                    continue;
                }
                // write the new java file
                writeNewFile(response.get(0), fileNames.get(i));
                System.out.println("Code separated and saved");
            } catch (Exception e) {
                System.err.println("The following error occurred for file " + fileNames.get(i) + ": " + e.getMessage());
            }
        }
        // log success message to console
        System.out.println("All refactor(s) complete");
    }

    private void createDirectoryIfNeeded(String directoryPath) {
        File directory = new File(directoryPath);
        if (!directory.exists()) {
            directory.mkdir();
        }
    }
}
