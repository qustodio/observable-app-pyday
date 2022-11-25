FROM python:3.11

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./app /opt/blueprints
WORKDIR /opt/blueprints

EXPOSE 8000
CMD python -m main

CMD python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload