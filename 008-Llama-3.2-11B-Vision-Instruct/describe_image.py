import os
import requests
import torch
from PIL import Image
from transformers import MllamaForConditionalGeneration, AutoProcessor
from huggingface_hub import login

# Get token from environment variable and login
hf_token = os.getenv("HUGGINGFACE_API_KEY")
if not hf_token:
    raise ValueError("Please set the HUGGINGFACE_API_KEY environment variable")

login(token=hf_token)

model_id = "meta-llama/Llama-3.2-11B-Vision-Instruct"
model = MllamaForConditionalGeneration.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    token=hf_token
)
processor = AutoProcessor.from_pretrained(
    model_id,
    token=hf_token
)

url = "https://raw.githubusercontent.com/dsikar/prompts/c5aec987d0c510b67d40c16d21e8bd500f1caaad/008-Llama-3.2-11B-Vision-Instruct/file.jpeg"
image = Image.open(requests.get(url, stream=True).raw)

messages = [
    {"role": "user", "content": [
        {"type": "image"},
        {"type": "text", "text": "Describe the image"}
    ]}
]
input_text = processor.apply_chat_template(messages, add_generation_prompt=True)
inputs = processor(
    image,
    input_text,
    add_special_tokens=False,
    return_tensors="pt"
).to(model.device)
output = model.generate(**inputs, max_new_tokens=30)
print(processor.decode(output[0]))
