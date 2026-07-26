from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

app = FastAPI()

openai.api_key = "YOUR_API_KEY"

class Input(BaseModel):
    text: str

@app.post("/analyze")
async def analyze(input: Input):

    prompt = f"""
You are a qualitative research AI.

Apply Braun & Clarke thematic analysis:

1. Familiarization
2. Coding
3. Theme generation
4. Theme review
5. Theme naming
6. Reporting

Context:
Phenomenological study of social workers & clients in Uganda.

Text:
{input.text}

Return JSON:
codes, categories, themes, quotes
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    result = response["choices"][0]["message"]["content"]

    return {
        "analysis": result,
        "graph": [
            {"data": {"id":"theme1","label":"Theme"}},
            {"data": {"id":"code1","label":"Code"}},
            {"data": {"source":"code1","target":"theme1"}}
        ]
    }
