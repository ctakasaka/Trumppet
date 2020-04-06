package main;

import java.io.*;
import java.net.*;
import java.io.File;
import java.io.PrintStream;
import java.io.ByteArrayOutputStream;
import org.alicebot.ab.Bot;
import org.alicebot.ab.Chat;
import org.alicebot.ab.MagicBooleans;
import org.alicebot.ab.MagicStrings;
import org.alicebot.ab.utils.IOUtils;
 
public class Chatbot {
    private static final boolean TRACE_MODE = false;
    static String botName = "trump";

    public static void main(String[] args) {
        try {
        	
        	// initializing bot and taking entries from python
            Chat chatSession = connect();
            
            
            System.out.println("Initializing connection to Python GUI...");
            // connecting to python via a socket to use python's simpler GUI
        	// using port 5000 as it is typically open
        	int portNumber = 5000;
        	
        	try(
        		ServerSocket serverSocket = new ServerSocket(portNumber);
        		Socket clientSocket = serverSocket.accept();
        		PrintWriter out = new PrintWriter(clientSocket.getOutputStream(),true);
        		BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));)
        	{
        		String userQuery;
        		while((userQuery = in.readLine()) != null) {
        			System.out.println(userQuery);
        			if(userQuery == null || userQuery.length() < 1)
        				userQuery = MagicStrings.null_input;
        			if(userQuery.contentEquals("bye")) {
        				out.println("Finally, I've got to get my golf count over 249! (Trump golf count is kept updated at www.trumpgolfcount.com)");
        				System.exit(0);
        			}
        			// now we query the bot
        			String reply = chatSession.multisentenceRespond(userQuery);
        			out.println(reply);
        			
        		} 
        	} catch(IOException e) {
        		System.out.println("Exception caught when trying to listen on port"+portNumber);
        		e.printStackTrace();
        	} catch(Exception e) {
        		e.printStackTrace();
        	}
        	
    
        	
//            String textLine = "";
//            int count = 1;
//            while(true) {
//                System.out.print(count+ ". You : ");
//                textLine = IOUtils.readInputTextLine();
//                if ((textLine == null) || (textLine.length() < 1))
//                    textLine = MagicStrings.null_input;
//                if (textLine.equals("q")) {
//                    System.exit(0);
//                }else {
//                    String request = textLine;
//                    String response = chatSession.multisentenceRespond(request);
//                    System.out.println("The Donald : " + response);
//                }
//                count++;
//            }
        } catch(Exception e) {
        	e.printStackTrace();
        }
    }
 
    private static String getResourcesPath() {
        File currDir = new File(".");
        String path = currDir.getAbsolutePath();
        path = path.substring(0, path.length() - 2);
        String resourcesPath = path + File.separator + "src" + File.separator + "main" + File.separator + "resources";
        return resourcesPath;
    }

    public static Chat connect(){
        // create mock output stream to avoid library output
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        PrintStream mockOut = new PrintStream(outputStream);

        // save original output stream for later
        PrintStream orig = System.out;
        System.setOut(mockOut);

        String resourcesPath = getResourcesPath();
        MagicBooleans.trace_mode = TRACE_MODE;
        Bot bot = new Bot(botName, resourcesPath);
        Chat chatSession = new Chat(bot);
        bot.brain.nodeStats();

        // return output stream from mock
        System.setOut(orig);

        return chatSession;
    }

}
