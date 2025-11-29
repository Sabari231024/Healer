FROM python:3.11-slim
WORKDIR /healer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY healer/ ./healer/
ENV GIT_CLONE_PATH=/repo
CMD ["uvicorn", "healer.main:app", "--host", "0.0.0.0", "--port", "8001"]
