# 🤖 ChatOllama + GenAI RAG Chatbot

This repository contains two AI-powered backend projects built using FastAPI + Ollama:

1. ChatOllama API (LLM Chat System)
2. GenAI RAG Chatbot (Document-based AI using RAG)

---

# 📌 Project 1: ChatOllama API

## 🚀 Overview
FastAPI backend that connects to Ollama local LLM models for chat responses.

## ⚙️ Features
- Chat with local AI models (Ollama)
- FastAPI REST API
- Lightweight and fast
- Easy frontend integration

## ▶️ Run Project

uvicorn app:app --host 0.0.0.0 --port 8000 --reload

Then open:
http://127.0.0.1:8000/

---

## 🧪 If not working (Windows)

& "C:\Users\Mohamed_Lotfy\AppData\Local\Programs\Python\Python311\python.exe" -m uvicorn app:app --reload

---

# 📌 Project 2: GenAI RAG Chatbot

## 🚀 Overview
AI chatbot that answers ONLY from document.txt using RAG (Retrieval-Augmented Generation).

## ⚙️ Features
- Document-based Q&A system
- RAG architecture
- Prevents hallucination
- Uses Ollama LLM

## 📄 How it works
1. Load document.txt
2. Split text into chunks
3. Retrieve relevant context
4. Send context to LLM
5. Generate answer

---

## ▶️ Run Project

uvicorn app:app --host 0.0.0.0 --port 8000 --reload

Open:
http://127.0.0.1:8000/

---

## 🧪 If not working (Windows)

& "C:\Users\Mohamed_Lotfy\AppData\Local\Programs\Python\Python311\python.exe" -m uvicorn app:app --reload

---

# 🛠 Tech Stack
Python | FastAPI | Ollama | RAG

---

# 🎯 Skills Demonstrated
- LLM Integration
- Backend API Development
- RAG Implementation
- AI System Design

---

# 💼 Open To Work
AI Engineer | Backend Developer | Full Stack Developer | .NET Developer