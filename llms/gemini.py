import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyAAD-JH2-2aokSn1cpYCVnQHf-XS7NSV0A"))

model = genai.GenerativeModel("gemini-pro")

def summarize(text, prompt="Summarize this AI paper:\n"):
    response = model.generate_content(prompt + text)
    return response.text.strip()
