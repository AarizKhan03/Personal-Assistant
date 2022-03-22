import speech_recognition as sr
import os
import subprocess

r = sr.Recognizer()
m = sr.Microphone()

r = sr.Recognizer()
on = True 

def for_website():
    counter = 0 # 3 tries before it terminates
    print("And what website would you like to go to?")
    while on :    
            with sr.Microphone() as source:
                audio = r.listen(source) #taking in audio input

                try:
                    web_name = r.recognize_google(audio) #storing speech as text in a variable
                    print("You said: {}".format(web_name))
                    f = open("TempWebsite.txt", "w")
                    f.write(web_name)
                    f.close() 
                    break
                except:
                    if counter < 3:
                        print("I Didn't Recognise What You Said. Could You Repeat That Please.")
                        counter += 1
                    else:
                        print("If you're trying to speak, please check your microphone and try again!")
                        break    
    os.system("g++ site_open.cpp -o site_open.exe")
    #os.system("./site_open.exe")
    subprocess.check_call(["site_open.exe"])
def for_app():
    counter = 0 # 3 tries before it terminates
    print("And what application would you like to open?")
    while on :    
            with sr.Microphone() as source:
                audio = r.listen(source) #taking in audio input

                try:
                    app_text = r.recognize_google(audio) #storing speech as text in a variable
                    print("You said: {}".format(app_text))
                    f = open("TempApp.txt", "w")
                    f.write(app_text)
                    f.close() 
                    break
                except:
                    if counter < 3:
                        print("I Didn't Recognise What You Said. Could You Repeat That Please.")
                        counter += 1
                    else:
                        print("If you're trying to speak, please check your microphone and try again!")
                        break
    os.system("g++ app_open.cpp -o app_open.exe")
    #os.system("./app_open.exe")
    subprocess.check_call(["app_open.exe"])
def for_youtube_search():
    counter = 0 # 3 tries before it terminates
    print("And what would you like to search for?")
    while on :    
            with sr.Microphone() as source:
                audio = r.listen(source) #taking in audio input

                try:
                    keywords = r.recognize_google(audio) #storing speech as text in a variable
                    print("You said: {}".format(keywords))
                    list_keywords = keywords.split()
                    keywords = "+".join(list_keywords)
                    f = open("TempYoutubeSearch.txt", "w")
                    f.write(keywords)
                    f.close() 
                    break
                except:
                    if counter < 3:
                        print("I Didn't Recognise What You Said. Could You Repeat That Please.")
                        counter += 1
                    else:
                        print("If you're trying to speak, please check your microphone and try again!")
                        break    
    os.system("g++ youtube_search.cpp -o youtube_search.exe")
    subprocess.check_call(["youtube_search.exe"])    
def for_google_search():
    counter = 0 # 3 tries before it terminates
    print("And what would you like to search for?")
    while on :    
            with sr.Microphone() as source:
                audio = r.listen(source) #taking in audio input

                try:
                    keywords2 = r.recognize_google(audio) #storing speech as text in a variable
                    print("You said: {}".format(keywords2))
                    list_keywords2 = keywords2.split()
                    keywords2 = "+".join(list_keywords2)
                    f = open("TempGoogleSearch.txt", "w")
                    f.write(keywords2)
                    f.close() 
                    break
                except:
                    if counter < 3:
                        print("I Didn't Recognise What You Said. Could You Repeat That Please.")
                        counter += 1
                    else:
                        print("If you're trying to speak, please check your microphone and try again!")
                        break    
    os.system("g++ google_search.cpp -o google_search.exe")
    subprocess.check_call(["google_search.exe"])
def voice_input():
    counter = 0 # 3 tries before it terminates
    print("Hi! What can I do for you?")
    while on :    
            with sr.Microphone() as source:
                audio = r.listen(source) #taking in audio input

                try:
                    input_text = r.recognize_google(audio) #storing speech as text in a variable
                    print("You said: {}".format(input_text))
                    f = open("TempVoice.txt", "w")
                    f.write(input_text)
                    f.close() 
                    break
                except:
                    if counter < 3:
                        print("I Didn't recognise what you said. Could you repeat that please.")
                        counter += 1
                    else:
                        print("If you're trying to speak, please check your microphone and try again!")
                        break
    if word_search(["open","website"],input_text) == True or word_search(["visit","website"],input_text) == True:
        for_website()
    elif word_search(["open","app"],input_text) == True or word_search(["open","application"],input_text) == True:    
        for_app()
    elif word_search(["search","video"],input_text) == True or word_search(["search","youtube"],input_text) == True or word_search(["video","youtube"],input_text) == True:
        for_youtube_search()
    elif word_search(["search","google"],input_text) == True:
        for_google_search()

def word_search(list_of_words,phrase):
    [x.lower() for x in list_of_words]
    phrase = phrase.lower()    
    if all(words in phrase for words in list_of_words):
        return True
    else:
        return False

voice_input()

            



