from openai import OpenAI
#import dotenv
#dotenv.load_dotenv()
#key = dotenv.get_key("OPENAI_API_KEY")
from env import API_KEY, BASE_URL # temporary workaround...

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