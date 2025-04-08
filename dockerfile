# Sử dụng Python base image
FROM python:3.10-slim

# Tạo thư mục làm việc
WORKDIR /app

# Copy file requirements và cài đặt
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ project vào container
COPY . .

# Chạy ứng dụng Flask
CMD ["flask", "--app", "main", "run", "--host=0.0.0.0"]
