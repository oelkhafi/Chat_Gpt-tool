># ChatGPT Refactoring Tool

This is a gradle plugin tool designed to offer developers refactoring suggestions within their active IntelliJ IDEA session, without having to externally access similar resources.


The project contains a folder named "pre_plugin_src", which contains the source code from the tool's logic development, as well as a folder named "plugin" which specifically houses the gradle project for the IntelliJ IDEA plugin.

If you wish to explore the tool's functionality, there is a file called "gpt_tool.mjs" & "new_script.mjs" which each house the raw logic, however, the gpt_tool houses it in an OOP format and new_script houses it in a script format.

If you are looking to download and use the tool, please note that it is still under development. The gradle project is set up for the plugin and there is an .xml file for plugin downloading, however, issues with the OpenAI dependencies have made it so the current version of the plugin is not available for download.

When exploring the functionality of the scripts, remember to add your own API_KEY (generated from OpenAI's API site) into a .env file.

If you would like to contact the team that worked on this project, their emails will be included below:

- Drew Carranti - acarrant@stevens.edu
- Lauren Kibalo - lkibalo@stevens.edu
- Joseph Weimer - jweimer@stevens.edu
- Omar Elkhafif - oelkhafi@stevens.edu