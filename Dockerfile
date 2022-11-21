FROM python:3.9.15-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY newSOumaya.py .

CMD ["python", "newSOumaya.py"]
