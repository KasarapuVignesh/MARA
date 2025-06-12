import fitz  # PyMuPDF

def summarize_pdfs(state):
    papers = state.get("papers", [])
    summaries = []

    for paper in papers:
        pdf_path = paper.get("pdf_path")
        if not pdf_path:
            continue
        try:
            doc = fitz.open(pdf_path)
            text = ""
            for page in doc:
                text += page.get_text()
            doc.close()
            summaries.append({
                "url":paper.get("pdf_url"),
                "title": paper.get("title"),
                "summary": text[:1000]  # first 1000 chars, placeholder
            })
        except Exception as e:
            print(f"Error reading {pdf_path}: {e}")
            summaries.append({
                "title": paper.get("title"),
                "url":paper.get("pdf_url"),
                "summary": "[Error reading PDF]"
            })

    return {**state, "summaries": summaries}

# import os
# import fitz  # PyMuPDF
# import google.generativeai as genai

# # Configure Gemini
# genai.configure(api_key=os.getenv("AIzaSyAAD-JH2-2aokSn1cpYCVnQHf-XS7NSV0A"))  # Ensure your API key is set
# model = genai.GenerativeModel("gemini-pro")

# def summarize_pdfs(state):
#     papers = state.get("papers", [])
#     summaries = []

#     for paper in papers:
#         pdf_path = paper.get("pdf_path")
#         title = paper.get("title", "Untitled")
#         pdf_url = paper.get("pdf_url", "")
#         if not pdf_path:
#             continue

#         try:
#             # Step 1: Extract PDF text
#             doc = fitz.open(pdf_path)
#             text = "".join(page.get_text() for page in doc)
#             doc.close()

#             # Step 2: Chunk (trim long papers)
#             chunked_text = text[:5000]

#             # Step 3: Generate summary with Gemini
#             prompt = (
#                 "Summarize this research paper in 5-6 lines:\n\n" + chunked_text
#             )
#             response = model.generate_content(prompt)
#             summary = response.text.strip()

#             # Step 4: Try extracting abstract from the full text
#             abstract = extract_abstract_from_text(text)

#             summaries.append({
#                 "title": title,
#                 "abstract": abstract,
#                 "summary": summary,
#                 "pdf_url": pdf_url
#             })

#         except Exception as e:
#             print(f"❌ Error reading {pdf_path}: {e}")
#             summaries.append({
#                 "title": title,
#                 "abstract": "[Error extracting abstract]",
#                 "summary": "[Error reading PDF]",
#                 "pdf_url": pdf_url
#             })

#     return {**state, "summaries": summaries}


# def extract_abstract_from_text(text: str) -> str:
#     """Simple function to extract abstract section from text."""
#     import re
#     match = re.search(r"(?i)(abstract)(.*?)(introduction|1\.|I\.)", text, re.DOTALL)
#     if match:
#         return match.group(2).strip()
#     return text[:500].strip()  # fallback
