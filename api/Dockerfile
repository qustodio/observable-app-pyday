FROM python:latest

ENV PYTHONPATH "${PYTHONPATH}:/opt/config/"

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /opt/api
WORKDIR /opt/api

RUN mkdir -p /opt/config/

EXPOSE 8000
CMD python -m uvicorn main:app --host 0.0.0.0 --port 8000