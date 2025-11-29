from fastapi import FastAPI
from .models import ErrorReport
from .patch_pipeline import process_error_and_create_pr

app = FastAPI()

@app.post("/report_error")
async def report_error(err: ErrorReport):
    pr = await process_error_and_create_pr(err)
    return {"status":"ok","pr":pr}
