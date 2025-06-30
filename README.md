# 🧠 DataAgentX

**AI-Powered Dataset Discovery Tool** for Kaggle & Hugging Face  
Built with Streamlit • Zero-Shot Classification • LLM-Generated Tags • Markdown Reporting

### 📸 Demo Screenshots

#### 🔍 Initial Search Interface  
This is the first screen where the user enters a dataset topic and chooses a source (Hugging Face or Kaggle).

![Search Interface](https://huggingface.co/spaces/mufithamajeed/dataagentx/resolve/main/App%20screenshot%201.png)

---

#### ✅ Search Results — Multiple Datasets Found  
This screen shows the result of the query with multiple datasets listed.

![Search Results](https://huggingface.co/spaces/mufithamajeed/dataagentx/resolve/main/App%20screenshot%202.png)

---

#### 🧠 Dataset Details with Tags and News Links  
Here, the user sees the dataset description, smart tags generated using LLMs, and external reference links.

![Tags and News](https://huggingface.co/spaces/mufithamajeed/dataagentx/resolve/main/App%20screenshot%203.png)

---


## 🚀 Overview

**DataAgentX** is a Streamlit-based tool that simplifies dataset discovery and selection using intelligent search and LLM tagging. It empowers data scientists, ML researchers, and developers to:

- 🔍 Search for datasets on **Hugging Face** or **Kaggle**
- 🧠 Generate **AI-based tags** using zero-shot classification (BART-MNLI)
- 📥 Download datasets to a local `/data/raw/` directory
- 📝 Export a professional markdown report of search results

---

## 📦 Features

- ✅ Hugging Face & Kaggle dataset search
- 🔍 Zero-shot classification of dataset descriptions via `transformers` pipelines
- 🧠 Automatic tagging with `facebook/bart-large-mnli`
- 📄 Report generator in markdown format
- 📥 Dataset downloader to `/data/raw/`
- 🧼 Clean Streamlit UI with theme switcher
- 🐳 Fully Dockerized
- 🚀 Deployable on [Hugging Face Spaces](https://huggingface.co/spaces)

---

## 🧑‍💻 Getting Started Locally

### 1. Clone the Repository
```bash
git clone https://github.com/mufithamajeed/dataagentx.git
cd dataagentx
```

### 2. Set Up Kaggle API Credentials

- Visit: [https://www.kaggle.com/account](https://www.kaggle.com/account)
- Create a new API token and download `kaggle.json`

Place the file in:
```bash
~/.kaggle/kaggle.json
```

Or set credentials via environment variables:
```bash
export KAGGLE_USERNAME=your_username
export KAGGLE_KEY=your_key
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
streamlit run app.py
```

---

## 🐳 Run with Docker

### Build the image
```bash
docker build -t dataagentx .
```

### Run the container
```bash
docker run -p 8501:8501 dataagentx
```

---

## 🗂 File Structure

```
dataagentx/
│
├── app.py                    # Main Streamlit app
├── agents/
│   └── llm_tagger.py         # LLM tag generation (zero-shot)
├── utils/
│   ├── search_hf.py          # Hugging Face dataset search
│   └── search_kaggle.py      # Kaggle dataset search
├── reports/                  # Markdown reports saved here
├── requirements.txt          # Python dependencies
└── Dockerfile                # For container deployment
```

---

## 📄 Example Output

**Tags + Download + Report**

![Example](https://huggingface.co/spaces/mufithamajeed/dataagentx/resolve/main/App%20screenshot%203.png)

---

## 📚 Tech Stack

- [Streamlit](https://streamlit.io/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- [Kaggle API](https://github.com/Kaggle/kaggle-api)
- [Hugging Face Datasets](https://huggingface.co/docs/datasets)
- [Docker](https://www.docker.com/)
- Python 3.9+

---

## 🌍 Live Demo

Try it live on [Hugging Face Spaces](https://huggingface.co/spaces/mufithamajeed/dataagentx)

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 🙌 Acknowledgements

Developed by [Mufitha Majeed](https://github.com/mufithamajeed)  
LLM-powered tagging powered by 🤗 `facebook/bart-large-mnli`

---

> Made with 💡 by combining AI and Open-Source

