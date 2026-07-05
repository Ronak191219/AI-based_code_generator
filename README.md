# 🤖 AI Code Generator

An AI-powered web application that generates source code from natural language prompts using Google's Gemini API. The application supports multiple programming languages through a simple Flask-based web interface.

---

## 📌 Features

- 🤖 AI-powered code generation using Google Gemini API
- 💻 Supports multiple programming languages (Python, Java, C++, JavaScript, HTML, CSS, SQL, React, Flask, etc.)
- ⚡ Fast and accurate code generation
- 🎨 Clean and responsive web interface
- 🔒 Secure API key management using environment variables (.env)
- ❌ Error handling for invalid API keys and API failures

---

## 🏗️ Architecture

User Input → Flask Backend → Gemini API → Generated Code → Web UI

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | HTML, CSS |
| Backend | Flask (Python) |
| AI Model | Google Gemini API |
| Environment | python-dotenv |

---

## 📸 Project Preview

(Add your screenshots here)

---

## 🚀 Installation

Clone the repository

```bash
git clone <your-repository-url>
cd AI-code-generator
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
python app.py
```

Open in browser

```
http://127.0.0.1:5000
```

---

## 📂 Project Structure

```
AI-code-generator/
│
├── app.py
├── requirements.txt
├── .env
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

---

## 👨‍💻 Author

**Ronak**