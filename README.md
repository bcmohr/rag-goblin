# RAG-Goblin Overview

A Python script for demonstrating a quick and simple integration of OpenAI's chat completion and embeddings functionalities for RAG. The script performs a cosine similarity search between an embedded user input string and a set of embedded database strings. It then uses these similarity scores to identify the most relevant database entries in for the user's query.

## Features

- Embeddings: Generates embeddings for text strings using the `embed` function from the `scripts.embeddings` module.
- Cosine Similarity: Calculates the cosine similarity between the embedding of the user input string and each database string using the `similar` function from the `scripts.similarity` module.
- Logging Support: Includes optional logging capabilities to provide insights into the script's operations, such as similarity scores and selected database entries.
- Chat Completion Integration: Uses the `chat_completion` function to generate a response based on the most relevant database entries, simulating a conversation with the user.

## Requirements

- Python 3.x
- OpenAI API access and appropriate API keys for chat completion and embeddings functionalities.
- `logging` module
- `numpy` module
- `python-dotenv` module (not presently needed. eventually, maybe?)

## Usage

- Enable Logging (Optional): Uncomment the `logging.basicConfig(level=logging.INFO)` line to enable logging.
- Define User and Database Strings: Customize the `input_str1` variable with the user's input and `input_str2` to `input_str5` with database entries.
- Generate Embeddings and Calculate Similarity: The script automatically generates embeddings for each input string and calculates cosine similarity scores.
- Identify Relevant Database Entries: Based on similarity scores, the script identifies the top two most relevant database entries.
- Generate Response: The script formats a request for the chat completion function, incorporating the most relevant database entries, and outputs a response.

## Customization

- Modify the user input and database strings as needed for different queries.
- Adjust logging settings to control the verbosity of script output.
- Update the chat completion request format according to specific requirements or to experiment with different response generation strategies.

## Repository Structure

- `scripts/`: Contains modules for embeddings generation (`embeddings.py`), similarity calculation (`similarity.py`), and chat completion (`completions.py`).
- `main.py`: Main script demonstrating the integration of embeddings, similarity search, and chat completion to process and respond to user queries.

## Final Notes
### 👉 😎 👉
