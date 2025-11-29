import httpx
from .config import LLM_SERVICE_URL

async def generate_completion(prompt: str, max_tokens: int = 512):
    async with httpx.AsyncClient(timeout=60.0) as c:
        r = await c.post(LLM_SERVICE_URL, json={
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": 0.2
        })
        r.raise_for_status()
        return r.json()["completion"]
