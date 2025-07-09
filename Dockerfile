FROM python:3.11-slim

WORKDIR /app

COPY requirement.txt .
RUN pip install -r requirement.txt
COPY app/ app/

CMD ["python", "app/main.py"]