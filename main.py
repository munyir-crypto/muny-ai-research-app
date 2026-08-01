from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

class Input(BaseModel):
    text: str

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/analyze")
async def analyze(input: Input):

    prompt = f"""
Perform thematic analysis (Braun & Clarke).

Text:
{input.text}

Return JSON with:
codes, themes, quotes
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return {"result": response["choices"][0]["message"]["content"]}