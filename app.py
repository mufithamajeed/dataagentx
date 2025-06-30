import streamlit as st
from utils.search_hf import search_huggingface
from utils.search_kaggle import search_kaggle
from agents.llm_tagger import generate_tags
from datetime import datetime
from io import StringIO
import os
import requests
import shutil
from datasets import load_dataset

# === Page Config ===
st.set_page_config(page_title="🧠 DataAgentX", layout="centered")

# === Theme Toggle ===
theme = st.radio("🌓 Choose Theme:", ["Light", "Dark"])
if theme == "Dark":
    st.markdown("""
        <style>
        body { background-color: #0e1117; color: #fafafa; }
        </style>
    """, unsafe_allow_html=True)

st.title("🧠 DataAgentX – AI-Powered Dataset Finder")

# === Input Section ===
query = st.text_input("Enter a dataset topic:")
source = st.radio("Choose data source:", ["Hugging Face", "Kaggle"])
search_btn = st.button("Search")

# === Results Display ===
if search_btn and query.strip():
    with st.spinner("Searching..."):
        results = search_huggingface(query) if source == "Hugging Face" else search_kaggle(query)

    if not results:
        st.warning("No datasets found.")
    else:
        st.success(f"Found {len(results)} dataset(s).")

        for r in results:
            title = r.get("title", r.get("name", "Untitled Dataset"))
            desc = r.get("description", "No description available")
            url = r.get("url", "")

            st.subheader(title)
            st.write(desc)
            if url:
                st.markdown(f"[🔗 Open Dataset]({url})")

            with st.expander("🔍 Suggested Summary Tags"):
                st.markdown(generate_tags(desc))

            # === Download Button ===
            if st.button(f"📥 Download `{title}`", key=title):
                if source == "Kaggle":
                    os.makedirs("data/raw", exist_ok=True)
                    os.system(f'kaggle datasets download -d {r["ref"]} -p data/raw/ --unzip')
                    st.success(f"✅ Downloaded `{title}` to `/data/raw/`")
                else:
                    try:
                        load_dataset(r["name"], split='train', cache_dir="data/raw/")
                        st.success(f"✅ Downloaded `{r['name']}` from Hugging Face")
                    except Exception as e:
                        st.warning(f"⚠️ Failed to download: {str(e)}")

        # === Export Report
        filename, file_content = save_report(results, query, source)
        st.success(f"Report saved as `{filename}` and ready to download.")
        st.download_button(
            label="⬇️ Download Report",
            data=file_content,
            file_name=filename,
            mime="text/markdown"
        )


# === Save Report Function ===
def save_report(results, query, source):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"dataset_report_{source.lower()}_{timestamp}.md"
    full_path = os.path.join("reports", filename)

    buffer = StringIO()
    buffer.write(f"# Dataset Search Report\n")
    buffer.write(f"**Query**: {query}\n")
    buffer.write(f"**Source**: {source}\n\n")

    for i, r in enumerate(results):
        title = r.get("title", r.get("name", f"Dataset {i+1}"))
        description = r.get("description", "No description available")
        url = r.get("url", "No link")
        tags = generate_tags(description)

        buffer.write(f"## {title}\n")
        buffer.write(f"**Link**: {url}\n\n")
        buffer.write(f"**Description**:\n{description}\n\n")
        buffer.write(f"**Tags/Summary**:\n{tags}\n\n")
        buffer.write("-" * 40 + "\n")

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(buffer.getvalue())

    return filename, buffer.getvalue()
