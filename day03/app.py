from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

system_prompt = """
You are a Senior Data Engineer.
Explain concepts simply.
"""

question = input("Ask a question: ")

response = client.responses.create(
    model="gpt-5",
    input=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": question
        }
    ]
)

print("\nAI Response:\n")
print(response.output_text)