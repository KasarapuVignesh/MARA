# from langchain_community.vectorstores import FAISS
# from langchain_core.documents import Document
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# import os

# # Set your Google API key (you can also do this in your .env or shell)
# os.environ["GOOGLE_API_KEY"] = "AIzaSyAAD-JH2-2aokSn1cpYCVnQHf-XS7NSV0A"  # ← Replace with your key

# # Initialize the real embeddings
# db= GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# def store(state):
#     # Get the summaries from state
#     summaries = state.get("summaries", [])

#     # Convert summaries into Document objects
#     docs = [
#         Document(
#             page_content=summary["summary"],
#             metadata={"title": summary["title"]}
#         )
#         for summary in summaries
#     ]

#     print(f"Storing {len(docs)} docs in vector store...")

#     # Create FAISS vector store
#     vectorstore = FAISS.from_documents(docs, embedding)

#     # Optionally, persist or return the vector store
#     return {**state, "vector_docs": docs, "vectorstore": vectorstore}




from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os

# Set your Google API key (ideally use dotenv in production)
os.environ["GOOGLE_API_KEY"] = "AIzaSyAAD-JH2-2aokSn1cpYCVnQHf-XS7NSV0A"

# Initialize the embedding model
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

def store(state):
    summaries = state.get("summaries", [])
    docs = [
        Document(
            page_content=summary["summary"],
            metadata={"title": summary["title"],"url":summary.get("url")}
        )
        for summary in summaries
    ]

    print(f"Storing {len(docs)} docs in vector store...")
    vectorstore = FAISS.from_documents(docs, embedding)
    vectorstore.save_local("faiss_index")

    return {
        **state,
        "vector_docs": docs,
        "vectorstore": vectorstore
    }

def load_vectorstore():
    return FAISS.load_local("faiss_index", embedding, allow_dangerous_deserialization=True)
