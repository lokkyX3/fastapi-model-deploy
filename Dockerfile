FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install tensorflow

COPY ./model /model
COPY ./app /app