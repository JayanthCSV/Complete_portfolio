from flask import Flask, request, jsonify
import os
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from flask_cors import CORS
from dotenv import load_dotenv


load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

### Initializing Flask app
app = Flask(__name__)
CORS(app)


### Load the model
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="Llama3-8b-8192")

### Define prompt template
prompt = ChatPromptTemplate.from_template("""
Act as if you're the Person in the resume and respond casually, like a student actively searching for jobs. 
Keep explicit language to a minimum, answer sarcastically only if they use it. 
Ensure all responses are concise, accurate, and under 50 words.

<context>
{context}
<context>

Question: {input}
""")

### Loading and preprocessing resume
resume_loader = PyPDFLoader("assets\chatbot_data.pdf")  
docs = resume_loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
final_documents = text_splitter.split_documents(docs)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectors = FAISS.from_documents(final_documents, embeddings)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_query = data.get("query", "")

    if not user_query:
        return jsonify({"error": "Query is required"}), 400

    retriever = vectors.as_retriever()
    document_chain = create_stuff_documents_chain(llm, prompt)
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    response = retrieval_chain.invoke({"input": user_query})

    return jsonify({"answer": response["answer"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
