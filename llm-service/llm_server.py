from fastapi import FastAPI
from pydantic import BaseModel
from llama_cpp import Llama

MODEL_PATH = "/models/qwen2.5-coder-1.5b-q4.gguf"

llm = Llama(model_path=MODEL_PATH, n_ctx=4096, n_threads=2)
app = FastAPI()

class GenerateRequest(BaseModel):
    prompt: str
    max_tokens: int = 512
    temperature: float = 0.2

class GenerateResponse(BaseModel):
    completion: str

@app.post("/generate", response_model=GenerateResponse)
def generate(req: GenerateRequest):
    out = llm(req.prompt, max_tokens=req.max_tokens, temperature=req.temperature, stop=["```"])
    return GenerateResponse(completion=out["choices"][0]["text"])
