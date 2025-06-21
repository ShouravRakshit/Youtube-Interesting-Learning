import openai
import base64
import os
from dotenv import load_dotenv
load_dotenv()


client = openai.OpenAI(
    base_url="https://api.sambanova.ai/v1",
    api_key=os.getenv("SAMBANOVA_API_KEY")
)

# Helper function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# The path to your image
image_path = "scary.jpg"

# The base64 string of the image
image_base64 = encode_image(image_path)

print(image_base64)

response = client.chat.completions.create(
    model="Llama-4-Maverick-17B-128E-Instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What is happening in this image?"},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}}
            ]
        }
    ]
)

print(response.choices[0].message.content)