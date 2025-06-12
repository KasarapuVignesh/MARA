import os
import requests

def download(state):
    papers = state["papers"]
    for paper in papers:
        response = requests.get(paper["pdf_url"])
        path = f"data/papers/{paper['title'][:50].replace('/', '_')}.pdf"
        with open(path, "wb") as f:
            f.write(response.content)
        paper["pdf_path"] = path
    return state
