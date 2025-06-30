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
