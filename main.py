import speech_recognition as sr
import subprocess
from time import strftime
import os
import time
import random


def Convert(string):
    li = list(string.split(" "))
    return li

# import playsound
# from gtts import gTTS
# def sofiaResponse(audio):
#     print(audio)
#     tts = gTTS(text=audio, lang="en")
#     filename = "asdf.mp3"
#     tts.save(filename)
#     playsound.playsound(filename)
#     os.remove(filename)
#     # if os.path.exists("asdf.mp3"):
#     #     os.remove("asdf.mp3")

# from gtts import gTTS
# from pygame import mixer
# def sofiaResponse(audio):
#     tts = gTTS(text=audio, lang='en')
#     tts.save('v2.mp3')
#     mixer.init()
#     mixer.music.load('v2.mp3')
#     mixer.music.play()
#     while mixer.music.get_busy():
#         time.sleep(1)


def sofiaResponse(audio):
    import pyttsx3  # sophia
    print(audio)
    engine = pyttsx3.init() #using HP Anna's voice
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    for line in audio.splitlines():
        engine.say(audio)
        engine.runAndWait()

def myCommand():
    # "listens for commands"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        print('Say something...')
        audio = r.listen(source)
        print("Time over, thanks")
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        command = myCommand();
    return command

def assistant(command):

    assistname = 'xyz '

# greetings
    if assistname + 'hey' in command:
        day_time = int(strftime('%H'))
        if day_time < 12:
            sofiaResponse('Hello Sir. Good morning')
        elif 12 <= day_time < 18:
            sofiaResponse('Hello Sir. Good afternoon')
        else:
            sofiaResponse('Hello Sir. Good evening')
    elif assistname + 'hello' in command:
        day_time = int(strftime('%H'))
        if day_time < 12:
            sofiaResponse('Hello Sir. Good morning')
        elif 12 <= day_time < 18:
            sofiaResponse('Hello Sir. Good afternoon')
        else:
            sofiaResponse('Hello Sir. Good evening')
    elif assistname + 'hi' in command:
        day_time = int(strftime('%H'))
        if day_time < 12:
            sofiaResponse('Hello Sir. Good morning')
        elif 12 <= day_time < 18:
            sofiaResponse('Hello Sir. Good afternoon')
        else:
            sofiaResponse('Hello Sir. Good evening')

# time
    elif assistname + 'time' in command:
        import datetime
        now = datetime.datetime.now()
        today = datetime.date.today()
        sofiaResponse('Current time is ' + str(now.strftime("%I:%M%p")) + " " + today.strftime("%A %B %d"))

# patient detail
    elif assistname + 'patient detail' in command:
        # import tkinter as tk
        # from tkinter import simpledialog
        # ROOT = tk.Tk()
        # ROOT.withdraw()
        # hospCOID = simpledialog.askstring(title="hospcoid", prompt="Hospital COID:")
        # account = simpledialog.askstring(title="account", prompt="Account:")
        # print(hospCOID + account)

        # import tkinter as tk
        # from tkinter import *
        # from tkinter import ttk
        # window = tk.Tk()
        # window.title("Welcome to TutorialsPoint")
        # window.geometry('400x400')
        # window.configure(background="grey");
        # a = Label(window, text="First Name").grid(row=0, column=0)
        # b = Label(window, text="Last Name").grid(row=1, column=0)
        # c = Label(window, text="Email Id").grid(row=2, column=0)
        # d = Label(window, text="Contact Number").grid(row=3, column=0)
        # a1 = Entry(window).grid(row=0, column=1)
        # b1 = Entry(window).grid(row=1, column=1)
        # c1 = Entry(window).grid(row=2, column=1)
        # d1 = Entry(window).grid(row=3, column=1)
        # def clicked():
        #     res = "Welcome to " + txt.get()
        #     lbl.configure(text=res)
        # btn = ttk.Button(window, text="Submit").grid(row=4, column=0)
        # window.mainloop()

        os.chdir('C:\\Users\\tnguye65\\Desktop\\Computer Coding\\!VBA Templates')
        os.system('start excel.exe "2 Patient Account Detail.xlsx"')
        sofiaResponse('You got it!')

# exhibit
    elif assistname + 'exhibit' in command:
        from PersonalAssist.resources_mac import AS400_exhibit
        def Convert(string):
            li = list(string.split(" "))
            return li
        splittingtext = Convert(command)
        exhibitnum = splittingtext[2]
        coid = splittingtext[4]
        if int(coid) <= 999:
            coid = "0"+str(coid)
        else:
            coid = str(coid)
        AS400_exhibit.main(coid, exhibitnum)
        sofiaResponse('You got it!')

# exhibit  xyz report 57 space 1471 space 93019
    elif assistname + 'report' in command:
        from PersonalAssist.resources_mac import AS400_report
        def Convert(string):
            li = list(string.split(" "))
            return li
        splittingtext = Convert(command)
        reportnum = splittingtext[2]
        coid = splittingtext[4]
        timeframe = splittingtext[6]
        if int(coid) <= 999:
            coid = "0" + str(coid)
        else:
            coid = str(coid)
        if int(timeframe) <= 99999:
            timeframe = "0" + str(timeframe)
        else:
            timeframe = str(timeframe)
        AS400_report.main(coid, reportnum, timeframe)
        sofiaResponse('You got it!')

# calculator
    elif assistname + 'calculator' in command:
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')
        sofiaResponse('You got it!')

# todolist
    elif assistname + 'to do list' in command:
        sofiaResponse('Yes sir')
        os.chdir('C:\\Users\\tnguye65\\Desktop\\Computer Coding\\!VBA Templates')
        f = open('todolist.txt', "r")
        lines = f.readlines()
        for line in lines:
            sofiaResponse(line)
        f.close()

    elif assistname + 'help me' in command:
        sofiaResponse(""" 
        You can use the following commands and I'll help you out:
        1. Hello 
        2. Time 
        3. Patient Detail 
        4. Calculator 
        5. To do List 
        """)
    elif assistname + 'exit' in command:
        sofiaResponse("Goodbye Sir, See you next time")
        exit()


sofiaResponse('Hi 10, XYZ here.')
if __name__ == '__main__':
    while True:
        assistant(myCommand())

