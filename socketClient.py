# used for Python to Java comm
import socket
import sys
import subprocess
from threading import Thread
import time
# spellchecking library
from spellchecker import SpellChecker
# basic, pretrained sentiment analyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#used for named entity recognition as well as POS
import spacy

# GUI requirements
import tkinter as tk
try:
    import ttk as ttk
    import ScrolledText
except ImportError:
    import tkinter.ttk as ttk
    import tkinter.scrolledtext as ScrolledText
from PIL import Image, ImageTk

# _init POS and named entity engine
pos = spacy.load("en_core_web_sm")

# _init spellcheck engine
spell = SpellChecker()

# _init sentiment engine
sentiment = SentimentIntensityAnalyzer()

# calling a thread to run the bot backend
startBot = ['java','-jar','ChatBot-1.1.jar','&']
print("Waking up Trump...\n")
subprocess.Popen(startBot)

topics = {}

conversationType = 'user'

HOST = '127.0.0.1'  # Localhost to reach Trumppet
PORT = 5000      # typically unused port
while 1:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
        except:
            time.sleep(1)
            continue

        if conversationType == "user":
            # GUI startup
            app = tk.Tk()
            app.title("Trumppet")
            app.configure(bg='orange')
            app.wm_resizable(0,0)

            window = ttk.Frame(app)
            # user submissions
            userSubmit = ttk.Button(window, text='Get Response', command="")
            userSubmit.grid(column=1, row=0, sticky='nesw', padx=3, pady=3)
            # user input field
            userInput = ttk.Entry(window, state='normal')
            userInput.grid(column=0, row=0, sticky='nesw', padx=3, pady=3)
            # text window
            conversation = ScrolledText.ScrolledText(window, state='disabled')
            conversation.grid(column=0, row=2, sticky='nesw', padx=10, pady=10)
            #image
            load = Image.open("trumppet.png")
            render = ImageTk.PhotoImage(load)
            logo = ttk.Label(window, image = render,background='orange')
            logo.grid(column = 1, row = 2)

            window.pack(padx=10,pady=50)
            window.mainloop()
            
            while 1:
                data = ""
                msg = input("Enter message: ")

                # spellchecking, first tokenize, then run through spelling engine
                msg = spell.split_words(msg)
                msg = [spell.correction(token) for token in msg]

                # rejoin tokens and passes to sentiment analysis
                query = " ".join(msg)
                score = sentiment.polarity_scores(query)['compound']
                print(score)

                # run through POS / named entity engine to get the user's topic
                things = pos(query)
                topicStuff = [[token.lemma_, token.text]for token in things if (token.dep_ == "dobj")]
            
                try:
                    topic = topicStuff[0][0]
                except:
                    topic = None
                if topic is not None:
                    # maintain set of topics user has spoken about
                    if topic not in topics.keys():
                        topics[topic] = 1
                    else:
                        topics[topic] += 1
                    print(topics.get(topic))
                    print(topicStuff[0][1])
                    if topics.get(topic) > 1:
                        if score > 0.2:
                            data = "I get that you like "+topicStuff[0][1]+" but please, please stop talking about it. Oh my."
                        elif score < -0.1:
                            data = "If you don't like "+topicStuff[0][1]+" stop talking about it. I want to get back to waving my arms in front of Americans."
                        else:
                            data = "As a great guy once said to me, the greatest guy by the way, stop talking about "+topicStuff[0][1]
                
                # encode and send message to Java if not predetermined by Python
                if data == "":
                    query = bytes(query+"\n",'utf8')
                    s.sendall(query)
                    data = s.recv(1024).decode("utf-8")
                print("Trump:",data)
                if "249" in data:
                    print('LobbyBot: He left, you can stay here alone now if you want... I guess?')

        elif conversationType == "otherBot":
            #IP = input("Enter their IP: ")
            IP = '154.20.16.74'
            #IP = '174.4.38.222'
            while 1:
                print("Attempting to connect...")
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as talk:
                    try:
                        talk.connect((IP,PORT))
                    except:
                        time.sleep(1)
                        continue

                    print('Connected')
                    while 1:
                        test = input("Enter message: ")
                        talk.sendall(bytes(test,'utf8'))
