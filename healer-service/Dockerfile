FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y git && apt-get clean
RUN pip install --no-cache-dir -r requirements.txt

# Copy healer package
COPY healer/ /app/healer/

EXPOSE 8001

CMD ["uvicorn", "healer.main:app", "--host", "0.0.0.0", "--port", "8001"]
