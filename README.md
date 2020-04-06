## Group 11 ChatBot - Trumppet
Jodi Chan 71966600, Erik Johnston 76035344<br/>
Wilson Stewart 34074823, Callum Takasaka 16835019

## Preface

### Unfortunately, it is currently understood that Gerardo Zamora 25330168 would not like to be associated with this rendition of group 11's final project, as such we are submitting this chatbot on behalf of the other 4 group members of group 11, as listed above.

### Had we known of this sooner, or been notified, we would have removed any work that was completed by Gerardo Zamora. We apologize that this was not possible.

## General Structure

    The basis of the chatbot is built upon an AIML capable Java chatbot, which we then defined rules for. This essentially means it can only ever be as smart as we write it out to be. We then used sockets to connect our Python frontend with the Java bot. 

    (We are unsure if sockets in this context will amount to extra marks)

## GUI

- Our GUI features the minimum number of fields required for a functional chatbot, this both improves simplicity and streamlines the look of the application.

- It was decided that the 'tkinter' Python library would be optimal for creating the GUI since a group member had previous experience working with it.

### GUI Example:

![Trumppet GUI](\2020-04-05-173321_1121x700_scrot.png "Trumppet Interface")

## Topics

### **Health & Wellness**

- Trumppet is able to suggest health tips both for fitness and diet, however the creators **STRONGLY** urge users to make sure Trumppet wasn't joking before taking its advice!

### **Coronavirus / Covid-19**

- In lieu of recent global events \**cough*\* pandemics, we decided that letting Trumppet help people get informed about the current Covid-19 outbreak could help 'flatten the curve'. These tips are a little bit more factual, but there is still humour hidden inside!

 If Trumppet encounters anything outside of general introductions and the above 2 topics, it has a selection of 7 different predetermined responses to choose from.

## Data Flow Diagrams

### Level 0

![Level 0 DFD](\level0DFD.jpg "Level 0 DFD")

The user sends messages to a Python GUI which then sends it to the bot. The bot then relays its response back to the GUI which displays it for the user.

### Level 1

![Level 1 DFD](\level1dfd.jpg "Level 1 DFD")

The user sends their message to the Python GUI which then runs the message through various processing techniques. First, a simple spellcheck is administered, followed by sentiment analysis and name entity analysis. This is accomplished in part by lemmatizing some portions of the text deemed to be potential topics. The processed message is then byte-encoded and sent to the bot through a localhost socket. The bot uses AIML expression to respond and sends the response back to the Python interface via the same socket. This is then displayed to the user via the GUI.

## GitHub Repository

Due to our unique situation, it is not possible to update the original repo with a new branch for our GUI implementation or any of our Python implementation. Therefore, we are just going to place all final code into a new repository and hope you understand the reasoning for this.

### GitHub link: https://github.com/ctakasaka/Trumppet

## Sample Conversation (With Feature Highlighting)

    1. User: hey
       Trumppet: What do you want. Who are you.
    2. User: my name is callum
       Trumppet: That is an awful name, who thought that was a good idea.
    3. User: who are you
       Trumppet: What do you mean "who am I?" I'm the greatest president of the greatest country in the world.
    4. User: what should i eat to lose weight
       Trumppet: Stop eating so much food. Drink the refreshing taste of Diet Coke.
    5. User: i like strawberries
       Trumppet: Strawberries? Really?

Repeated use of a topic either positively or negatively facilitates a different response

    6. User: i really really like strawberries (NAMED ENTITY RECOGNITION / POS) (SENTIMENT ANALYSIS)
       Trumppet: I get that you like strawberries but please, please stop talking about it. Oh my.
    7. User: should i exercise
       Trumppet: Yes, you will never get my perfect orange body if you don't tan and workout.
    8. User: what are the best exercises
    Trumppet: Run, Swim, Lift, anything you clearly are not doing fatty.
    9. User: is there anything wrong with being vegan
       Trumppet: Vegan diet is the worst diet.
    10.  User: how about the keto diet
        Trumppet: I have been told that keto can work, if you are willing to try anything to get a body like mine I would reccomend trying keto.
    11.  User: peanuts taste weird
        Trumppet: Peanuts are technically not nuts, they are legumes. I know this because my intellect is so large, larger than most.
    12.  User: so do you like golf
        Trumppet: I do like golf, i like it very much
    13.  User: what programming language do you like
        Trumppet: I grew up with Java but not that i am rich it is definitely ruby, god i love money
    14.  User: what language are you gonna learn next
        Trumppet: I want to learn python but i am scared of snakes
    15.  User: how far away should i stay away from people now with this coronavirus stuff
        Trumppet: At least 2 metres away
    16.  User: what if i start having difficulty breathing is that a sign
        Trumppet: Yes covid makes it quite difficult to breathe
    17.  User: i have a runny nose right now is that bad
        Trumppet: It is not, thanksfully our noses are safe
    18.  User: what if i have a fever
        Trumppet: That is concerning, go and get tested for the virus. Except not in the us cause we aren't doing that here
    19. User: is it true that you arent able to taste if you have coronavirus
        Trumppet: If you cant taste you probably already have corona, don't touch me
    20. User: should i travel right now
        Trumppet: Travelling would be a good idea if you hated everyone in the world
    21. User: does canada have enough masks to supply its citizens
        Trumppet: Canada definitely has masks, i definitely didn't ask the company that makes them to not ship them to Canada nope.
    22. User: i heard that you thought covid was a hoax
        Trumppet: I never said that I will have you arrested right now if i ever hear you say that again i am the smartest
    23. User: i am unimaginably bored trump
        Trumppet: Hello, unimaginably bored trump. I've met many unimaginably bored trumps, the best unimaginably bored trump, even. But you, you're different. You may be the best unimaginably bored trump now.
    24. User: wow good one im so bored seriously what do i do
        Trumppet: I know you are bored, but just go play tennis and swim in the pool at your house its not that bad
    25. User: is it true that you arent able to taste if you have coronavirus
        Trumppet: If you cant taste you probably already have corona, don't touch me

Random response from a predefined list

    26. User: the guord is very green (UNHANDLED DIALOGUE)
        Trumppet: I might be too smart to understand what you are saying

Random response from a predefined list

    27. User: she sold seashells by the seashore (UNHANDLED DIALOGUE)
        Trumppet: If you want to talk to me you must say something meaningful as i am extremely smart

Repeated use of a topic facilitates a response, even if it is a previously unhandled topic

    28. User: she sold many seashells by the seashore (NAMED ENTITY RECOGNITION / POS)
        Trumppet: As a great guy once said to me, the greatest guy by the way, stop talking about seashells

Random response from a predefined list

    29. User: i hate dogs (UNHANDLED DIALOGUE)
        Trumppet: Sorry i don't speak italian

Repeated use of a topic negatively or positively facilitates a response, even if it is a previously unhandled topic

    30. User: i hate dogs a lot trump (NAMED ENTITY RECOGNITION / POS) (SENTIMENT ANALYSIS)
        Trumppet: If you don't like dogs stop talking about it. I want to get back to waving my arms in front of Americans.
    31. User: bye
        Trumppet: Finally, I've got to get my golf count over 249! (Trump golf count is kept updated at www.trumpgolfcount.com)

        LobbyBot: He left, you can stay here alone now if you want... I guess?

### Limitations

- Cannot handle some specific spelling errors
- Narrow scope of topics
- Not the handiest of tips!
- Lacks robust data storage
- Used AIML, largely outdated and non-dynamic

## Potential APIs

### Python to Java Socket Communication

Using our socket system, you can easily run Java and Python together for a wombo-combo of epic proportions.

### Sentence-wide Spellchecker

Our spellchecker handles both tokenization of a sentence and the parsing of each token, which could be helpful in many other projects. Only works for english though.

### GUI Frame

Our GUI easily extended to more fields and uses a grid system, making it very easy to change for different needs. The functions baked into the GUI are also handy in running something very quickly as a prototype.

### Background Java execution in Python

Using internal system calls with a built-in Python library, you can run (in our case) a Java jar executable directly within a Python program. This makes it easier to handle as the Java program becomes a child process of the Python script!

### Topic Extraction

Our named entity recognition combined with lemmatization allows for quickly grabbing the topic in a sentence or phrase. This can be altered to grab the subject or action as well.

## List of Features

We decided to integrate Python into our project since we had some experience working with libraries that could improve our chatbot, such as the GUI and the natural language processing

### Basic, Generalized Spellchecking

- General spellchecking was implemented by tokenizing sentences and parsing through each token to both validate and correct and potential spelling errors. This was achieved by using the 'autocorrect' Python library. (applied upon user input, so internal)

### Sentiment Analysis

- We implemented sentiment analysis with the 'nltk' library, using their pretrained engine called 'Vader' to give our bot an idea of how the user felt about certain topics.

### Name Entity Recognition & POS

- These were implemented using the 'spaCy' library, by parsing through each user message and pulling out the topic of interest. This allowed our bot, combined with the above sentiment recognition, to respond dynamically if a user frequently talks about a topic, positively or negatively.

### Lemmatization

- To pull out topics accurately, we used lemmatization which allowed the bot to pick out a general topic in any of its word forms.
- Used internally

These snippets demonstrate most of the features listed above

        User: i really really like strawberries (NAMED ENTITY RECOGNITION / POS) (SENTIMENT ANALYSIS)
        Trumppet: I get that you like strawberries but please, please stop talking about it. Oh my.

        User: i hate dogs a lot trump (NAMED ENTITY RECOGNITION / POS) (SENTIMENT ANALYSIS)
        Trumppet: If you don't like dogs stop talking about it. I want to get back to waving my arms in front of Americans.

## Requirements / How to Run

         1. Clone the GitHub repository
         2. pip install pyspellchecker
         3. pip install spacy
            1. python -m spacy download en_core_web_sm
         4. pip install nltk
            1. python3
               1. > import nltk
               2. > nltk.download('vader')
         5. pip install pillow
         6. Run GUI_Test.py

Tkinter should already be downloaded on your machine, however instructions can be found here if necessary: https://www.activestate.com/products/tcl/