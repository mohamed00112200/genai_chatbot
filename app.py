from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

app = FastAPI()

# ⚡ Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # accessible from any device
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend
@app.get("/")
def index():
    return FileResponse("frontend/index.html")


# Load FAISS
embeddings = OllamaEmbeddings(model="nomic-embed-text")
db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)
retriever = db.as_retriever(search_kwargs={"k": 3})  # top 3 chunks

# LLM using Gemma3:1b
llm = ChatOllama(model="gemma3:1b")

# Prompt template
prompt = ChatPromptTemplate.from_template("""
Answer the question using only the context below.

Context:
{context}

Question:
{question}
""")

# Chain: retriever → prompt → LLM
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
)

# Request model
class Question(BaseModel):
    question: str

@app.post("/ask")
def ask(q: Question):
    response = chain.invoke(q.question)
    return {"answer": response.content}
