package chatbottests;


import org.alicebot.ab.Chat;
import org.junit.Test;
import static org.junit.Assert.assertEquals;



public class Test_Bot_Responses {

    // For each response to check one must change the expected and actual variable to their corresponding interactions
    @Test
    public void Response(){
        Chat c = main.Chatbot.connect();
        assertEquals("Hey lazy human. I am here to help you with you diet and exercise\n" +
                "You can also ask me to tell a joke, I have the best jokes, the best!",c.multisentenceRespond("Hello"));
    }
}

