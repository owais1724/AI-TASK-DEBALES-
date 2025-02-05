# Langchain AI Chatbot for Technical Courses

This project demonstrates how to create a custom AI chatbot that extracts information from a website, generates embeddings, stores them in a FAISS vector store, and provides a Flask-based REST API to interact with users. The chatbot provides information about technical courses from Brainlox.

## Features
- **Web Scraping**: Loads technical course information from the Brainlox website.
- **Embedding Generation**: Uses OpenAI embeddings to convert the content into vector representations.
- **Vector Search**: Uses FAISS for fast similarity search over the document embeddings.
- **Flask REST API**: Provides an API endpoint to interact with the chatbot via HTTP POST requests.
- **OpenAI Integration**: Uses GPT-4 for generating natural language responses based on the extracted context.

## Requirements

- Python 3.x
- OpenAI API Key
- Flask
- Langchain
- FAISS
- OpenAI Python Client

