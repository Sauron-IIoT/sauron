FROM python:3.8-slim

RUN pip install pipenv

COPY . .
RUN pipenv install --system

ENV PYTHON_PATH=.

CMD ["python", "run.py"]