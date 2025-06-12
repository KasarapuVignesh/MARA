import arxiv

def scrape(state):
    search = arxiv.Search(
        query="Artificial Intelligence",
        max_results=3,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    papers = []
    for result in search.results():
        papers.append({
            "title": result.title,
            "pdf_url": result.pdf_url,
            "abstract": result.summary,
            "published": result.published,
        })
    state["papers"] = papers
    return state
