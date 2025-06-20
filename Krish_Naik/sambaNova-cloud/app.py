# SambaNova asynchronous example using OpenAI Python SDK
# This example demonstrates how to use the SambaNova API with the OpenAI Python SDK in an asynchronous context.
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
import asyncio
load_dotenv()

async def main():
    client = AsyncOpenAI(
        base_url="https://api.sambanova.ai/v1", 
        api_key=os.getenv("SAMBANOVA_API_KEY")
    )
    completion = await client.chat.completions.create(
        model="Meta-Llama-3.1-8B-Instruct",
        messages = [
            {"role": "system", "content": "Answer the question in a couple sentences."},
            {"role": "user", "content": "Share a happy story with me"}
        ]
    )
    print(completion.choices[0].message.content)
asyncio.run(main())