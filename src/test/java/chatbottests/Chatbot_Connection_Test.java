package chatbottests;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;
import main.Chatbot;
import org.alicebot.ab.Chat;
import org.junit.Test;

public class Chatbot_Connection_Test {

    @Test
    public void testConnection(){
        try {
            Chat c =  Chatbot.connect();
            assertEquals("trump",c.bot.name);
        }catch (Exception e){
            fail();
        }
    }
}
