# 🧠 DataAgentX

**AI-Powered Dataset Finder using Streamlit + Hugging Face + Kaggle**

---

## 🔍 Overview

**DataAgentX** is a Streamlit-based web application that helps researchers, developers, and data enthusiasts discover relevant datasets from Hugging Face and Kaggle based on a simple keyword query.

It integrates:
- 🧠 Large Language Model (LLM) tagging (optional module)
- 🔍 Search across Hugging Face Hub and Kaggle Datasets
- 📄 Auto-generated markdown reports
- 🌙 Light/Dark mode toggle
- 📥 Dataset downloader
- 🚀 One-click deployment on Hugging Face Spaces

---

## 🖥️ Features

- **Keyword Search**: Type any topic (e.g., "climate", "healthcare") and get results instantly.
- **Multi-source Support**: Choose between Hugging Face or Kaggle as your dataset source.
- **Auto Report Generator**: Export your dataset search results into a markdown report.
- **Tag Generator (LLM)**: [Coming soon] Summarizes dataset descriptions into tags using an LLM.
- **Dark Mode Toggle**: Switch between light and dark modes.
- **Download Button**: Download datasets directly (Hugging Face only).
- **Streamlit Interface**: Fully interactive and easy to use.
- **Free Deployment**: Host your app on Hugging Face Spaces for free!

---

## 🚀 Quickstart (Local)

```bash
# Clone the repository
git clone https://github.com/mufithamajeed/dataagentx.git
cd dataagentx

# Create a virtual environment
python -m venv env
# Activate it (Windows)
.\env\Scripts\activate
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 🗂️ Project Structure

```
dataagentx/
│
├── app.py                   # Streamlit frontend
├── requirements.txt         # Python dependencies
├── .streamlit/              # Theme & config settings
│   └── config.toml
├── reports/                 # Saved markdown reports
├── utils/                   # Search logic scripts
│   ├── search_hf.py         # Hugging Face search
│   ├── search_kaggle.py     # Kaggle search
│   └── llm_tagger.py        # [Optional] LLM-based tag generator
└── README.md
```

---

## ☁️ Deployment (Hugging Face Spaces)

**Steps:**

1. Visit [https://huggingface.co/spaces](https://huggingface.co/spaces)  
2. Click **Create New Space** → Choose `Docker` + `Streamlit`  
3. Upload the entire project folder including:
   - `app.py`
   - `requirements.txt`
   - `.streamlit/config.toml`
   - `utils/` and `reports/` folders

4. Add the following `Dockerfile` to your repo:

```dockerfile
FROM python:3.9

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
```

5. Done! Your app should go live shortly.

---

## 📌 Roadmap

- ✅ Hugging Face + Kaggle Search
- ✅ Markdown Report Export
- ✅ Hugging Face dataset downloader
- ✅ Hugging Face Spaces deployment
- 🔄 LLM-based tag summarization module
- ⏳ Dataset preview and advanced filters
- ⏳ Search history and saved bookmarks

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♀️ Author

**Mufitha Majeed**  
🔗 [GitHub](https://github.com/mufithamajeed)  
🌐 [Hugging Face Spaces](https://huggingface.co/spaces/mufithamajeed)

---
