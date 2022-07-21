
from gtts import gTTS
import sys
import os
import random 
from playsound import playsound

# mytext = 'Welcome to geeksforgeeks!'
mytext = str(random.randint(100000,999999)) 
language = 'en'
mytext =  list(mytext)
mytext = " ".join(mytext)
myobj = gTTS(text=mytext, lang=language, slow=False)


myobj.save("PTR.mp3")
print(mytext)

