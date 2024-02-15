from openai import OpenAI
#import dotenv
#dotenv.load_dotenv()
#key = dotenv.get_key("OPENAI_API_KEY")
from env import API_KEY, BASE_URL # temporary workaround...

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