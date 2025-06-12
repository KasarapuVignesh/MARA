import streamlit as st
from agents.vector_store import load_vectorstore

st.set_page_config(page_title="AI Paper Summarizer", layout="wide")
st.title("🧠 Latest AI Paper Summaries")

try:
    db = load_vectorstore()
except Exception as e:
    st.error("❌ Error loading vector store: " + str(e))
    db = None

if db is None:
    st.warning("⚠️ Run `main.py` first to generate vector data.")
else:
    st.subheader("📰 Latest Papers (Title + Abstract Preview)")
    try:
        docs = db.similarity_search("Artificial Intelligence", k=3)
        for doc in docs:
            st.markdown("### 📄 " + doc.metadata.get("title", "Untitled"))
            st.write(doc.page_content[:1000] + "...")
            #st.write(doc.metadata.get("urls"))
            pdf_url = doc.metadata.get("url","")
            if pdf_url:
               st.markdown(f"[📄 View PDF]({pdf_url})", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"❌ Error fetching papers: {e}")
        

    st.divider()

    #query = st.text_input("Ask a question about the papers (e.g. 'What is reinforcement learning?')")
    
    if st.button("Show Summary"):
        results = db.similarity_search("Artificial Intelligence")
        if not results:
            st.info("❌ No results found for your query.")
        else:
            st.subheader("🔍 Results")
            for doc in results:
                  st.markdown("### 📄 " + doc.metadata.get("title", "Untitled"))
                  st.write(doc.page_content[:3000])
    else:
        st.info("⬆️ You can ask questions about the papers above.")
