import os 
import speech_recognition as sr
from speech_recognition import Microphone, Recognizer, UnknownValueError

import sounddevice as sd
import ChatTTS

import warnings

from transformers import pipeline
import torch

chat = ChatTTS.Chat()
chat.load(compile=True)


pipe = pipeline("text-generation", 
                model="google/gemma-2-2b-it", 
                model_kwargs={"torch_dtype": torch.float32},  # Using float32 for CPU compatibility
                device="cpu",)  # Use cpu instead of GPU 

def AskAI(prompt, previousResponses):
    prompt = prompt + ". Answer in brief."
    allPrevResponse = ""
    for previousResponse in previousResponses:
        allPrevResponse += previousResponse + "/n"
    messages = [
        {"role": "user", "content": allPrevResponse + "/n" + prompt},
    ]
    outputs = pipe(messages, max_new_tokens=256)
    assistant_response = outputs[0]["generated_text"][-1]["content"].strip()
    return assistant_response

previousResponses = []

def audio_callback(recognizer, audio):
    try: 
        prompt = recognizer.recognize_whisper(
            audio, model="base", language="english"
        )

        texts = [ " How are you ?"]

        params_infer_code = ChatTTS.Chat.InferCodeParams (
                temperature = .3,
                top_P = 0.7,
                top_K = 20
        )
        wavs = chat.infer(texts, params_infer_code = params_infer_code)
        sd.play (wavs[0][0], 24000, blocking= True)
        print("\033[92m >> You: " + prompt + "\033[0m")
        
        wavs = chat.infer("Give me one minute", params_infer_code = params_infer_code)
        sd.play (wavs[0][0], 24000, blocking= True)
        
        response = AskAI(prompt, previousResponses)
        previousResponses.append(response)
        texts = [ response ]

        wavs = chat.infer(texts, params_infer_code = params_infer_code)
        sd.play (wavs[0][0], 24000, blocking= True)

        print("\033[93m >> Hal900:", response, " \033[0m")
        if "bye" in prompt.lower():
            stop_listening(wait_for_stop=False)
            os._exit(0)
    except UnknownValueError:
        print("Didnt understand, try again")

r = Recognizer()
microphone = Microphone(device_index=1)

with microphone as source: 
    r.adjust_for_ambient_noise(source)

stop_listening = r.listen_in_background(microphone, audio_callback)

print("Hello Dave")
input()
stop_listening(wait_for_stop=False)
    
