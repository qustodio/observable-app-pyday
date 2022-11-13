FROM python:latest

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY api /opt/api
WORKDIR /opt/api
