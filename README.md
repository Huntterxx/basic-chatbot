# basic-chatbot

# 🤖 Llama 3.3 70B Chatbot

A powerful AI chatbot powered by **Llama 3.3 70B** and utilizing the **OpenRouter API** for intelligent conversation. The backend is deployed on **Render**, and the frontend runs on **Streamlit**.

## 🚀 Features
- Uses **Llama 3.3 70B** for natural language understanding.
- Backend API powered by **FastAPI**, hosted on **Render**.
- Frontend built with **Streamlit**, deployed on **Streamlit Community Cloud**.
- Secure API integration using OpenRouter.

## 🛠️ Installation

### Clone the Repository
```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### Install Dependencies
Make sure you have Python 3.12+ installed.
```sh
pip install -r requirements.txt
```

### Run Backend (FastAPI)
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Run Frontend (Streamlit)
```sh
streamlit run app.py
```

## 🚢 Deployment
- **Backend:** Deployed on **Render**.
- **Frontend:** Hosted on **Streamlit Community Cloud**.

## 🔑 API Key Security
To prevent exposing your OpenRouter API key:
- Store it in an `.env` file (for local use).
- Use environment variables in your deployment.

## 📜 License
This project is open-source. Feel free to contribute! 🎉
