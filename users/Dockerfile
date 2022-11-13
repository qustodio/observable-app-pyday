FROM python:3.10.8

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir -p /opt/users
COPY ./main.py /opt/users/main.py