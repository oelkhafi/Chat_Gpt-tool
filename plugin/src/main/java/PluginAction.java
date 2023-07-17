import com.intellij.openapi.actionSystem.AnAction;
import com.intellij.openapi.actionSystem.AnActionEvent;

import tool.gpt.GptTool;

public class PluginAction extends AnAction {
    @Override
    public void actionPerformed(AnActionEvent e) {
        // create a new instance of the GptTool class
        GptTool tool = new GptTool();
        // refactor the files
        tool.refactorFiles();
    }
}
