import os
import openai

# Set the OpenAI API key
api_key = "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"
openai.api_key = api_key

# Load the document
document = """
The quick brown fox jumps over the lazy dog.
The dog barks at the cat.
The cat chases the mouse.
The mouse squeaks in fear.
"""

# Split the document into three different documents
documents = document.split("\n")

# Ask a question
question = "What is the color of the fox?"

# Set the prompt
prompt = document

# Get the relevant document
relevant_document = openai.ChatCompletion.create(
model="davinci",
messages=[                                               # The system message is just a placeholder
{"role": "system", "content": "You are a helpful assistant."},
{"role": "user", "content": question},
],

# The documents parameter is a list of documents that the chat completion can use to answer the question
documents=documents,

# The max_tokens parameter limits the length of the chat completion's response
max_tokens=100,
prompt=prompt
)

# Get the answer from the chat completion
answer = relevant_document.choices[0].message.content

# Print the answer
print(answer)




# Expected output
# The fox is red.









''' the langchain module does not have a get_relevant_document() function. This is because the langchain module is not a general-purpose library for natural language processing. It is a specialized library for creating and using language chains. A language chain is a sequence of words that are linked together by their meaning. The langchain library provides functions for creating, storing, and querying language chains.

To get the relevant document, you can use the openai.ChatCompletion.create() function. This function takes an embeddings parameter, which allows it to get the relevant document more accurately.



'''