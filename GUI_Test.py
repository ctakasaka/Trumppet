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

import tkinter as tk
try:
    import ttk as ttk
    import ScrolledText
    
except ImportError:
    import tkinter.ttk as ttk
    import tkinter.scrolledtext as ScrolledText
import time
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

        class TrumppetGUI(tk.Tk):

            def __init__(self, *args, **kwargs):
                """
                Create & set window variables.
                """
                tk.Tk.__init__(self, *args, **kwargs)
                

                self.title("Trumppet")
                self.configure(bg='orange')
                self.wm_resizable(0,0)
                self.initialize()

            def initialize(self):
                """
                Set window layout.
                """
                self.grid()



                self.respond = ttk.Button(self, text='Get Response', command=self.get_response)
                self.respond.grid(column=1, row=0, sticky='nesw', padx=3, pady=3)

                self.usr_input = ttk.Entry(self, state='normal')
                self.usr_input.grid(column=0, row=0, sticky='nesw', padx=3, pady=3)

                self.conversation = ScrolledText.ScrolledText(self, state='disabled')
                self.conversation.grid(column=0, row=2, sticky='nesw', padx=10, pady=10)

                #image
                self.load = Image.open("trumppet.png")
                self.render = ImageTk.PhotoImage(self.load)
                self.img = ttk.Label(self, image = self.render,background='orange')
                self.img.grid(column = 1, row = 2)
                

            def get_response(self):
                """
                Get a response from the chatbot and display it.
                """

                data = ""
                # take in user message
                msg = self.usr_input.get()
                self.usr_input.delete(0, tk.END)
                # spellchecking, first tokenize, then run through spelling engine
                msg = spell.split_words(msg)
                #msg = [spell.correction(token) for token in msg]
                for word in msg:
                    word = spell.correction(word)
                    if word == "veto":
                        word = "keto"

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
                    if topic not in topics.keys() and topic is not "what":
                        topics[topic] = 1
                    else:
                        topics[topic] += 1
                    print(topics.get(topic))
                    print(topicStuff[0][1])
                    if topics.get(topic) > 1:
                        if score > 0.2:
                            data = "I get that you like "+topicStuff[0][1]+" but please, please stop talking about it. Oh my."+"\n"
                        elif score < -0.1:
                            data = "If you don't like "+topicStuff[0][1]+" stop talking about it. I want to get back to waving my arms in front of Americans."+"\n"
                        else:
                            data = "As a great guy once said to me, the greatest guy by the way, stop talking about "+topicStuff[0][1]+"\n"

                # encode and send message to Java if not predetermined by Python
                if data == "":
                    querySend = bytes(query+"\n",'utf8')
                    s.sendall(querySend)
                    data = s.recv(1024).decode("utf-8")

                self.conversation['state'] = 'normal'
                self.conversation.insert(
                    tk.END, "User: " + query + "\n" + "Trumppet: " + data + "\n"
                )
                if "249" in data:
                    self.conversation.insert(tk.END, 'LobbyBot: He left, you can stay here alone now if you want... I guess?')
                self.conversation['state'] = 'disabled'
                print("User: " + query + "\n" + "Trumppet: " + data + "\n")
                            
                
                #user_input = self.usr_input.get()
                #self.usr_input.delete(0, tk.END)

                #self.conversation['state'] = 'normal'
                #self.conversation.insert(
                #    tk.END, "Human: " + user_input + "\n" + "ChatBot: " + str(response) + "\n"
                #)
                #self.conversation['state'] = 'disabled'

                time.sleep(0.5)


        trumppet_GUI = TrumppetGUI()
        trumppet_GUI.mainloop()
