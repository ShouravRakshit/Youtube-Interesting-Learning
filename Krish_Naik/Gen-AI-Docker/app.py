from fastapi import FastAPI
from transformers import pipeline

# create a new fastapi app instance
app = FastAPI()

# inititalize the text generation pipeline

pipe = pipeline("text2text-generation", model="google/flan-t5-small")

@app.get("/")
def home():
    return {"message": "Welcome to the Text Generation API"}

# Define a function to handle the GET request at `/generate`
@app.get("/generate")
def generate(text:str):
    # Use the pipeline to generate text based on the input
    output = pipe(text)

    # Return the generated text
    return {"generated_text": output[0]['generated_text']}