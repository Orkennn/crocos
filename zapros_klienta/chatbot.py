# chatbot.py

from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

model_name = "gpt2-medium"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

model.eval()


def generate_response(question):

    input_ids = tokenizer.encode(question, return_tensors="pt")

    with torch.no_grad():
        output = model.generate(input_ids, max_length=100, num_return_sequences=1)

    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response
