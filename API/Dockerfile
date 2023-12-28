FROM python:3.10.6-buster

# pip install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY main.py main.py
COPY setup.py setup.py
RUN pip install .

COPY Model Model

CMD uvicorn main:app --host 0.0.0.0 --port $PORT
