from  gtts import gTTS

from playsound import playsound

audio = "speech.mp3"

language ="en"

sp = gTTS(text= "Happy Birthday Dheeraj,God bless you ",lang=language,slow =False)

sp.save(audio)

playsound(audio)