from gtts import gTTS
from playsound import playsound

file = open("lyrics.txt","r",encoding="utf-8")
textt = file.read()
print(textt)

audio = gTTS(text=textt,lang="en",slow=False)
print("Emepetriando....")
audio.save("audio.mp3")

print("Playing...")
playsound("audio.mp3")