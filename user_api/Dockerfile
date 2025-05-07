FROM python:latest


WORKDIR /app
COPY . /app

RUN pip install --upgrade pip 
RUN pip install --no-cache-dir -r /app/requirments.txt

# EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]