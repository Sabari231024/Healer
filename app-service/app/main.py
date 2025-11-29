from fastapi import FastAPI
from .self_heal import self_heal

app = FastAPI()

@app.get("/ping")
async def ping():
    return {"status": "ok"}

@app.get("/divide")
@self_heal
async def divide(x: float, y: float):
    return {"result": x / y}
