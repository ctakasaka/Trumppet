package updatetests;

import static org.junit.Assert.assertEquals;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

import org.apache.commons.io.FileUtils;
import org.junit.Test;

public class Test_Update_AIML_Files {
	
	 	@Test
	    public void testUpdate() throws IOException {
	 		String resourcesPath = getResourcesPath();
            File dir = new File(resourcesPath+File.separator+"bots"+File.separator+"trump"+File.separator+"aiml");
	 		File source = new File(dir,"testcopyNoUse.aiml");
	 		File dest = new File(dir,"testNotUse.aiml");
	 	    FileUtils.copyFile(source, dest);
	 		update.Update_AIML_FILES.main(null);
	 		
	 		assertEquals(dest,new File(dir,"testNotUse.aiml"));
	 		dest.delete();

	 	}
	 	
	    private static String getResourcesPath() {
	        File currDir = new File(".");
	        String path = currDir.getAbsolutePath();
	        path = path.substring(0, path.length() - 2);
	        System.out.println(path);
	        String resourcesPath = path + File.separator + "src" + File.separator + "main" + File.separator + "resources";
	        return resourcesPath;
	    }
}
