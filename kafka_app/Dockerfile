FROM python:latest


WORKDIR /kafka_app
COPY . /kafka_app

RUN pip install --upgrade pip 
RUN pip install --no-cache-dir -r /kafka_app/requirments.txt

CMD python producer.py & python consumer.py