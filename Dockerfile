FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY mynmap.py .
ENTRYPOINT ["python", "mynmap.py"]
