from transformers import pipeline
import torch

pipe = pipeline("text-generation", 
                model="google/gemma-2-2b-it", 
                model_kwargs={"torch_dtype": torch.float32},  # Using float32 for CPU compatibility
<<<<<<< HEAD
                device="cpu",)  # Use cpu instead of GPU 
=======
                device="cpu",)  # Correct argument for limiting new tokens
>>>>>>> 083f260e (First Commit: Adding basic text to text converstation using Gemma through hugging face)

def generate_text(prompt, previousResponses):
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

while True: 
    user_input = input("\033[92m >> You: \033[0m")
    response = generate_text(user_input, previousResponses)
    previousResponses.append(response)
    print("\033[93m >> Hal900:", response, " \033[0m")
    
