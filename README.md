This project implements a voice-interactive assistant using speech recognition and text-to-speech synthesis. Hal9001 listens to the user’s voice, processes the input, generates a response using a language model, and then speaks the response back to the user.

Installation
1. Clone the repository:
bash
Copy
git clone https://github.com/FarKai/Hal9001
cd Hal900
2. Install dependencies:
Create a virtual environment (optional but recommended):
python -m venv venv
venv/bin/activate
Install required packages using pip:]
pip install -r requirements.txt
Ensure you have the following dependencies in the requirements.txt:

Copy
speechrecognition
sounddevice
torch
transformers
ChatTTS
Usage
Run the assistant:
To start the assistant, run the script:

python Hal900.py

Interacting with the assistant:
The assistant will listen for your voice input and respond verbally. You can ask the assistant questions, and it will generate and speak back responses. To stop the assistant, say “bye” to exit the loop.

How it works
Speech Recognition:

The assistant uses the speech_recognition library to listen to the user’s microphone input.

The input is processed using Whisper’s base model to convert speech into text.
Text Generation:

The assistant utilizes the Hugging Face transformers library to generate responses.
The model used is google/gemma-2-2b-it, which generates text-based answers to the prompts.
Text-to-Speech (TTS):

The ChatTTS library is used for text-to-speech conversion.
The assistant synthesizes speech based on the generated responses and plays the audio back to the user using the sounddevice library.
Interaction:

The assistant listens continuously for speech input and processes it using a callback function.
When the user provides input, the assistant generates a response and speaks it back.
The assistant stops if "bye" is detected in the input.
Dependencies
speechrecognition: For converting speech to text.
sounddevice: For playing audio responses.
ChatTTS: For text-to-speech synthesis.
transformers: For generating natural language responses.
torch: For running the transformers model.
Notes:
Ensure that your microphone is connected and properly configured.
The ChatTTS library may require certain configurations or pretrained models to work properly, so ensure you have everything set up.
Let me know if you need additional clarification or if you run into any issues!
