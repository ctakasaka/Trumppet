package update;

import java.io.File;
import java.io.IOException;
import org.alicebot.ab.Bot;
import org.alicebot.ab.MagicBooleans;

public class Update_AIML_FILES {
	private static final boolean TRACE_MODE = false;
    static String botName = "trump";
 
    public static void main(String[] args) {
        try {
 
            String resourcesPath = getResourcesPath();
            MagicBooleans.trace_mode = TRACE_MODE;
            Bot bot = new Bot(botName, resourcesPath);
            
            File dir = new File(resourcesPath+File.separator+"bots"+File.separator+"trump"+File.separator+"aimlif");
            deleteDataFiles(dir);
            
            bot.writeAIMLFiles();                                
 
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    private static String getResourcesPath() {
        File currDir = new File(".");
        String path = currDir.getAbsolutePath();
        path = path.substring(0, path.length() - 2);
        System.out.println(path);
        String resourcesPath = path + File.separator + "src" + File.separator + "main" + File.separator + "resources";
        return resourcesPath;
    }
    
    public static void deleteDataFiles(File dir) throws IOException {
    	File[] files = dir.listFiles();
        for (int i = 0; i < files.length; i++) {
          File file = files[i];        
            file.delete();  
          }
    }        
}
