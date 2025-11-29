FROM python:3.11-slim
RUN apt-get update && apt-get install -y build-essential
WORKDIR /llm
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY llm_server.py .
CMD ["uvicorn", "llm_server:app", "--host", "0.0.0.0", "--port", "8002"]
