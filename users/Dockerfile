FROM python:3.11

ENV PYTHONPATH "${PYTHONPATH}:/opt/config/"

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./src /opt/users
RUN mkdir -p /opt/config/

EXPOSE 8000

WORKDIR /opt/users
CMD python -m uvicorn main:app --host 0.0.0.0 --port 8000