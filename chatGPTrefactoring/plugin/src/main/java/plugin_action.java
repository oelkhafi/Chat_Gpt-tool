// import config from .env
import { config } from "dotenv";
config();
// other imports
import com.intellij.openapi.actionSystem.AnAction;
import com.intellij.openapi.actionSystem.AnActionEvent;
import gpt_tool;


public class PluginAction extends AnAction {
    @Override
    public void actionPerformed(AnActionEvent e) {
        gptTool refactoringTool = new gptTool();
        refactoringTool.refactorFiles();
    }
}
