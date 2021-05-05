import speech_recognition as sr
import time
from time import ctime
import webbrowser
import playsound
import os
import random
from gtts import gTTS

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            swart_speaks(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            swart_speaks('Sorry, I did not get that')
        except  sr.RequestError:
            swart_speaks('Sorry, my speech service is down')
        return voice_data

def swart_speaks(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
    


def respond(voice_data):
    if 'what is your name' in voice_data:
        swart_speaks('My name is swart')
    if 'what time is it' in voice_data:
        swart_speaks(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        swart_speaks('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('Send me your location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        swart_speaks('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()
    

time.sleep(1)
swart_speaks('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
