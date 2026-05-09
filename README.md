# AI Customer Support Agent

A lightweight AI-powered customer support system built using Flask, Ollama (Llama 3), and Google Text-to-Speech (gTTS).

This project demonstrates a **hybrid AI architecture** combining:
- Rule-based intent handling (fast deterministic responses)
- Local LLM fallback using Ollama (Llama 3)
- Text-to-speech voice generation
- Simple interactive web UI

---

## 🚀 Features

- AI-powered customer support assistant
- Local LLM inference using Ollama + Llama 3
- Hybrid routing system:
  - Keyword-based intent detection
  - LLM fallback for unseen queries
- Text-to-speech (TTS) audio generation using gTTS
- Flask REST API backend
- Simple web-based chat interface
- Audio playback for AI responses

---

## 💬 Example Queries

You can try the following:

- What is my loan balance?
- When is my payment due?
- How much is the late fee?
- I want to speak to customer care

---

## Tech Stack

### Backend
- Python
- Flask
- Ollama
- Llama 3
- gTTS

### Frontend
- HTML
- CSS
- JavaScript

---

## 🧠 System Architecture

```text
User (Frontend UI)
        ↓
Flask Backend (/chat API)
        ↓
Intent Router (Keyword Matching)
        ↓
 ┌───────────────┐
 │ Rule Match?    │── Yes → Predefined Response
 └───────────────┘
        ↓ No
Ollama LLM (Llama 3)
        ↓
Generated Response
        ↓
gTTS (Text → Speech)
        ↓
Response + Audio returned to UI
```
---

## 🔑 Key Design Decisions
```text
Hybrid architecture improves latency for common queries
Local LLM (Ollama) ensures privacy and offline capability
Separation of concerns:
backend handles logic + LLM + TTS
frontend handles UI only
Stateless API design for simplicity
```

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd customer-service-agent
```

### 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
# venv\Scripts\activate    # Mac
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install and run Ollama
```bash
ollama serve
```

### 5. Pull LLaMA 3 model
```bash
ollama pull llama3
```

### 6. Run Flask backend
```bash
python app.py
```

### 7. Open application
```bash
http://127.0.0.1:5001
```

## 📂 Project Structure

```text
customer-service-agent/
│
├── app.py                  # Flask backend
├── templates/
│   └── index.html         # Frontend UI
├── responses/             # Generated audio files
├── requirements.txt       # Dependencies
├── .gitignore             # Ignored files
└── README.md
```
