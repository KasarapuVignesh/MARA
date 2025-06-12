# 🧠 MULTI AGENT RESEARCH SUMMARIZER(AI Paper Summarizer)

An automated pipeline to fetch, summarize, and explore the latest Artificial Intelligence research papers from **arXiv.org**, powered by **LangChain**, **FAISS**, and **Google Gemini embeddings**. Designed with a daily scheduler that updates the system at **11:50 PM IST**.

---

## 🚀 Features

- ⏰ **Daily Paper Fetching:** Automatically fetches the 3 latest AI research papers from arXiv every night at **11:50 PM**.
- 📄 **PDF Download:** Downloads the full paper PDFs locally.
- ✂️ **Text Summarization:** Uses an LLM (e.g., Gemini) to generate summaries from paper abstracts or full content.
- 🔍 **Semantic Search:** Stores summaries in a FAISS vector database for similarity search and question answering.
- 🌐 **Streamlit UI:** Lets users view paper previews and ask questions about recent research papers.

---

## 🧱 Project Structure

├── agents/
│ └── vector_store.py # Handles FAISS storage and Google Gemini embedding
├── components/
│ ├── scraper.py # Fetches latest AI papers from arXiv
│ ├── downloader.py # Downloads PDFs of the papers
│ └── summarizer.py # Summarizes paper abstracts/full texts
├── graph/
│ └── pipeline.py # LangGraph pipeline that runs the full process
├── streamlit_app.py # UI for querying and viewing papers
├── main.py # Entry script to run the full pipeline manually
├── scheduler.py # Cron scheduler to auto-run main.py daily
├── .env # API keys and sensitive config (use dotenv)
├── requirements.txt
└── README.md # You are here


---

## 🔁 Daily Workflow (Scheduled at 11:50 PM IST)

### 🛠️ Trigger
A scheduler (`scheduler.py`) is configured using `schedule` or `cron` to invoke the pipeline daily at **11:50 PM**.

### 📦 Pipeline Stages

#### 1. `scraper.py`
- Uses the `arxiv` Python library.
- Queries the **3 latest Artificial Intelligence** papers.
- Stores metadata like:
  - `title`
  - `abstract`
  - `published date`
  - `pdf_url`

#### 2. `downloader.py`
- Takes metadata from the scraper.
- Downloads each paper’s PDF from the `pdf_url`.
- Stores them in `data/papers/`.

#### 3. `summarizer.py`
- Processes abstract (or content from the PDF if needed).
- Uses Gemini Pro or similar LLM to create a summary.
- Saves title, summary, abstract, and source URL.

#### 4. `vector_store.py`
- Embeds summaries using `GoogleGenerativeAIEmbeddings` from `langchain_google_genai`.
- Uses `FAISS` to store the vectorized documents.
- Saves the vector index to `faiss_index/`.

#### 5. `pipeline.py`
- Combines the above steps into a LangGraph node graph.
- Easily extendable to support multiple document types or sources.

---

## 💡 Streamlit App: `streamlit_app.py`

This is the user-facing interface where:
- The 3 latest papers are listed with:
  - **Title**
  - **Abstract snippet**
  - **Source URL (PDF)**
- Users can enter queries like:
  - *“What is reinforcement learning?”*
  - *“Explain the contribution of paper X”*
- The app returns **semantic results** using vector similarity search.

---

## 🔐 API Key Setup

You must add your **Gemini API key** to `.env` file:


Or, on **Streamlit Cloud**, add it in `st.secrets`.

---

## ✅ How to Run Manually
bash
Step 1: Install dependencies
pip install -r requirements.txt

 Step 2: Set up .env
echo "GOOGLE_API_KEY=your_key_here" > .env

 Step 3: Run full pipeline
python main.py

 Step 4: Run Streamlit UI
streamlit run streamlit_app.py
python scheduler.py
