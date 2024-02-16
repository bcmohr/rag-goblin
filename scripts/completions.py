from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# LLM chat completion function
def chat_completion(request_str):
    response = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[
            {"role": "system", "content": "You are a helpful RAG assistant. Respond concisely."},
            {"role": "user", "content": request_str}
        ]
    )
    response_str = response.choices[0].message.content
    return response_str

if __name__ == "__main__":
    print(chat_completion("What is the meaning of life?"))