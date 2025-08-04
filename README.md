# 🍽️ BiteAtlas

**BiteAtlas** is a Streamlit-powered chatbot app that uses **Dify AI** to help users explore:

- 🥘 Local foods  
- 🗺️ Famous dishes  
- 📍 Nearby places  

It supports:
- 🧠 Multiple chat sessions
- 💬 Real-time AI responses
- 🔒 Secure API key management via `secrets.toml`

---

## 🚀 Features

- Chat with an AI about food, restaurants, and travel tips  
- Sidebar with session history and "New Chat" functionality  
- Lightweight and mobile-friendly design  
- Secrets are managed securely (not pushed to GitHub)

---

## 🛠️ Setup & Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/BiteAtlas.git
   cd BiteAtlas
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Create .streamlit/secrets.toml

toml
Copy
Edit
DIFY_API_KEY = "your-dify-api-key"
Run the app

bash
Copy
Edit
streamlit run app.py
🧪 Tech Stack
Streamlit

Dify AI

Python, REST API, Markdown

📦 Deployment
To deploy on Streamlit Cloud:

Push your code (without .streamlit) to GitHub

Go to Streamlit Cloud → New app → Connect repo

Add DIFY_API_KEY under Secrets in Streamlit Cloud settings

🛡️ Note
Do NOT commit .streamlit/secrets.toml. Keep your API keys safe!

📄 License
MIT License
