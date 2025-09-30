import os, json
from openai import OpenAI

MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

_client = None
def client():
    global _client
    if _client is None:
        print("API KEY loaded?", bool(os.getenv("OPENAI_API_KEY")))
        _client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    return _client

def chat_json(system: str, user: str, temperature: float = 0.2) -> dict:
    resp = client().chat.completions.create(
        model=MODEL,
        messages=[{"role":"system","content":system},{"role":"user","content":user}],
        temperature=temperature,
    )
    content = resp.choices[0].message.content.strip()
    try:
        # Some models wrap JSON in backticks or text; try to extract first JSON block
        start = content.find("{")
        end = content.rfind("}")
        if start != -1 and end != -1:
            content = content[start:end+1]
        return json.loads(content)
    except Exception as e:
        # Fallback to return raw text for debugging
        return {"_raw": content, "_error": str(e)}
