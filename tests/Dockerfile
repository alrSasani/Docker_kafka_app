# Dockerfile.test
FROM python:3.9
WORKDIR /tests
COPY requirements-test.txt .
RUN pip install -r requirements-test.txt
COPY . /tests/
# CMD ["pytest", "tests/"]
CMD ["tail", "-f", "/dev/null"]