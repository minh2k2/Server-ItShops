FROM python:3.10-slim

WORKDIR /app

# Cài gói cần thiết cho mysqlclient
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

