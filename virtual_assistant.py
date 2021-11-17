import pyttsx3

import os

engine = pyttsx3.init()

pyttsx3.speak("Enter number to open application:\n")

while True:
    print("Enter number to open application: \n")
    print("\n1.Microsoft Word\t 2. Microsoft Excel\t 3. Google chrome \t 4. Microsoft edge \t 5. Notepad \t 0.Exit")




    p=input()

    p = p.upper()

    print(p)

    if ("DONT" in p) or ("DON'T" in p ) or("NOT " in p):
        pyttsx3.speak("Type again")
        print(".")
        print(".")
        continue
    elif ("3" in p):
        pyttsx3.speak("starting google chrome")
        os.system("start chrome")
        
    elif ("4"in p):
        pyttsx3.speak("startingmicrosoft edge")
        os.system("start msedge")

    elif ("5" in p):
        pyttsx3.speak("starting notepad")
        os.system("start notepad")

    elif ("1" in p):
        pyttsx3.speak("starting microsoft word")
        os.system("start winword")

    elif ("2"in p):
        pyttsx3.speak("starting microsoft excel")
        os.system("start excel")

    elif("0"in p):
        pyttsx3.speak("Exiting")
        break
    else:
        pyttsx3.speak(p)
        print("Is invalid . please try again")
        pyttsx3.speak("Is invalid please try again")

pyttsx3.speak("Dhiraj , you are  real python Programmer ")
 
