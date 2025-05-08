# Dockerfile.test
FROM python:3.9
WORKDIR /app
COPY requirements-test.txt .
RUN pip install -r requirements-test.txt
COPY . .
CMD ["pytest", "tests/"]