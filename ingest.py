from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

# تحميل النص
loader = TextLoader("data.txt", encoding="utf-8")
documents = loader.load()

# تقسيم النص
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)
chunks = splitter.split_documents(documents)

# Embeddings (Ollama)
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# إنشاء FAISS
db = FAISS.from_documents(chunks, embeddings)
db.save_local("faiss_index")

print("✅ Vector DB created successfully")
