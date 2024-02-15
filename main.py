from scripts.completions import chat_completion
from scripts.embeddings import embed
from scripts.similarity import similar
import logging
#logging.basicConfig(level=logging.INFO) # Uncomment this line to enable logging

#%%

# Example user input string
input_str1 = "which has just one cat?"
# Example database strings
input_str2 = "This is another test string for embedding. This one mentions dogs."
input_str3 = "This is a third test string for embedding. This one mentions cats."
input_str4 = "This is a fourth test string for embedding. This one mentions dogs and cats."
input_str5 = "DOC#1. Contents: 30,000 cats. Notes: Definitely not the appropriate path forward."

# Embed each string
em1 = embed(input_str1)
em2 = embed(input_str2)
em3 = embed(input_str3)
em4 = embed(input_str4)
em5 = embed(input_str5)

# Calculate the cosine similarity between each string and the input string
similarity_1_2 = similar(em1, em2)
similarity_1_3 = similar(em1, em3)
similarity_1_4 = similar(em1, em4)
similarity_1_5 = similar(em1, em5)
logging.info(f"💬 Similarity between 1 and 2: {similarity_1_2}")
logging.info(f"💬 Similarity between 1 and 3: {similarity_1_3}")
logging.info(f"💬 Similarity between 1 and 4: {similarity_1_4}")
logging.info(f"💬 Similarity between 1 and 5: {similarity_1_5}")

# Return the top two most similar inpt_str* to input_str1
top_two_similar = sorted([(similar(em1, em2), input_str2), (similar(em1, em3), input_str3), (similar(em1, em4), input_str4), (similar(em1, em5), input_str5)], reverse=True)[:2]
logging.info(f"💬 Result 1: Score={top_two_similar[0][0]}, String={top_two_similar[0][1]}")
logging.info(f"💬 Result 2: Score={top_two_similar[1][0]}, String={top_two_similar[1][1]}")

#%%

# Format the request to the chat completion function
request_str = f"""### Instructions:
You are a RAG system. Respond to the user's input. You must include information from the database as necessary. Don't mention "database". Just inform the user.

### User input:
{input_str1}

### Embedding cosine similarity search results:
#### Top result:
{top_two_similar[0][1]}
#### Second result:
{top_two_similar[1][1]}
"""
logging.info(f"💬 Request string: {request_str}")

#%%

# Call the chat completion function to get the response
response_str = chat_completion(request_str)
logging.info(f"💬 Response string: {response_str}")

#%%

print("\nRESULTS")
print(f"💬 User input: {input_str1}")
print(f"🤖 Response: {response_str}")