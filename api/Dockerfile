FROM python:latest

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /opt/api
WORKDIR /opt/api

CMD uvicorn main:app --reload --host 0.0.0.0