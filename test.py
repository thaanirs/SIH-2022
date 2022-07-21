from gtts import gTTS
import playsound
myobj = gTTS(text = "One",lang='en',slow=False)
myobj.save("hp.mp3")
playsound.playsound("hp.mp3")
#  playsound("hp.mp3")