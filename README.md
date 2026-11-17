# 🤖 AI Research Chat Agent

A persistent, web-deployable AI research chat assistant built with Python, Streamlit, and the official Google GenAI SDK, powered by `gemini-3.5-flash-lite`.

🌐 **Live Demo:** [Try the live app here!](https://share.streamlit.io/) *(https://my-ai-agent-8wrbpl8qgeinvfpdxsaxs5.streamlit.app/)*

---

## 🚀 Features

* **Persistent Chat Sessions:** Maintains full conversation context and history using Streamlit session state.
* **Modern Web Interface:** Clean, responsive chat UI built with Streamlit.
* **Live Session Export:** Allows users to download the complete chat session logs anytime directly from the sidebar.
* **Cloud Ready:** Optimized for seamless deployment on Streamlit Community Cloud.

---

## 🛠️ Tech Stack

* **Python** — Core programming language
* **Google GenAI SDK (`google-genai`)** — Official SDK for Gemini 3.5 Flash-Lite
* **Streamlit** — Framework for the interactive web application UI
* **Python-Dotenv** — Environment variable management

---

## 🔒 Security & API Key Management

To prevent accidental leaks of your private API keys to public version control, this project uses a dual security strategy:

1. **Local Environment (`.env`):** Local development uses a `.env` file to load the `GEMINI_API_KEY`. This file is completely excluded from Git tracking via `.gitignore`.
2. **Cloud Secrets (`st.secrets`):** On Streamlit Community Cloud, secrets are injected securely through the platform's dashboard configuration rather than being hardcoded or committed to GitHub.

---

## How to Run Locally

If you wish to run the application locally on your machine:

1. Clone the repository:
   `git clone https://github.com/alfrddb/my-ai-agent.git`

2. Move into the directory:
   `cd my-ai-agent`

3. Install dependencies:
   `pip install -r requirements.txt`

4. Run the app:
   `streamlit run main.py`

---

## Disclaimer

This project is intended for educational and portfolio purposes only.

---

## Author

**Alfredo De Biasio**  
- GitHub: [github.com/alfrddb](https://github.com/alfrddb)  
- LinkedIn: [Alfredo De Biasio](https://it.linkedin.com/in/alfredo-de-biasio-193603378)
