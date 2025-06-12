from langgraph.graph import StateGraph
from langchain_core.runnables import Runnable
from typing import TypedDict, List
from agents import scraper, downloader, summarizer, vector_store

# 1️⃣ Define your state schema
class PaperState(TypedDict):
    urls: List[str]
    files: List[str]
    texts: List[str]
    summaries: List[str]

# 2️⃣ Import or define your nodes (must return updated state dict)
def scrape_node(state: PaperState) -> PaperState:
    urls = scraper.scrape(state)
    return {**state, "urls": urls}

def download_node(state: PaperState) -> PaperState:
    files = downloader.download(state["urls"])
    return {**state, "files": files}

def summarize_node(state: PaperState) -> PaperState:
    texts = summarizer.summarize_pdfs(state["files"])
    return {**state, "texts": texts, "summaries": texts}  # simple reuse

def store_node(state: PaperState) -> PaperState:
    vector_store.store(state["summaries"])
    return state

# 3️⃣ Build the graph with schema
def build_graph() -> Runnable:
    builder = StateGraph(PaperState)  # ✅ FIXED

    builder.add_node("scrape", scrape_node)
    builder.add_node("download", download_node)
    builder.add_node("summarize", summarize_node)
    builder.add_node("store", store_node)

    builder.set_entry_point("scrape")
    builder.add_edge("scrape", "download")
    builder.add_edge("download", "summarize")
    builder.add_edge("summarize", "store")
    builder.set_finish_point("store")

    return builder.compile()
