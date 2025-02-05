from langchain.document_loaders import WebBaseLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from flask import Flask, request, jsonify
import openai
import os

# Set OpenAI API Key (Replace with your own key or use environment variable)
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"

# Step 1: Load Data from the URL
url = "https://brainlox.com/courses/category/technical"
loader = WebBaseLoader(url)
documents = loader.load()

# Step 2: Generate Embeddings
embeddings = OpenAIEmbeddings()
vector_store = FAISS.from_documents(documents, embeddings)

# Save the vector store
data_path = "faiss_index"
vector_store.save_local(data_path)

# Step 3: Create Flask REST API
app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    user_query = request.json.get("message")
    if not user_query:
        return jsonify({"error": "Message is required"}), 400
    
    docs = vector_store.similarity_search(user_query, k=3)
    context = "\n".join([doc.page_content for doc in docs])
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant providing information on technical courses."},
            {"role": "user", "content": user_query + "\n\nContext:\n" + context}
        ]
    )
    
    return jsonify({"reply": response["choices"][0]["message"]["content"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
