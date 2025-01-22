import os 
import speech_recognition as sr
from speech_recognition import Microphone, Recognizer, UnknownValueError


def audio_callback(recognizer, audio):
    try: 
        prompt = recognizer.recognize_whisper(
            audio, model="base", language="english"
        )
        print(prompt)
        if "bye" in prompt.lower():
            stop_listening(wait_for_stop=False)
            os._exit(0)
    except UnknownValueError:
        print("Didnt understand, try again")

r = Recognizer()
microphone = Microphone(device_index=1)
with microphone as source: 
    print("Good morning master")
    r.adjust_for_ambient_noise(source)
stop_listening = r.listen_in_background(microphone, audio_callback)
input()
stop_listening(wait_for_stop=False)
