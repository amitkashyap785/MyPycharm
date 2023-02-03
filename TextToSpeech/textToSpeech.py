
from gtts import gTTS   # we have imported this module for text to speech conversion
import os

# if you want from file that you can change this
abc = open('sample.txt')
text = abc.read()  # "hello guys, how are you. all fine?" text that you want to convert

language = 'en'

obj = gTTS(text=text, lang=language, slow=False)
# we have used slow = False because our converted video will have a high speed

obj.save("sample.mp3")

# to open the video file automatically we have to import os

os.system("sample.mp3")
