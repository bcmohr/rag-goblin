from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# Embedding function
def embed(input_str):
    response = client.embeddings.create(
        input=input_str,
        model="text-embedding-3-small"
    )
    return response.data[0].embedding

if __name__ == "__main__":
    print(embed("What is the meaning of life?"))