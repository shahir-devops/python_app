FROM python:3.15.0a8-alpine3.23
WORKDIR /
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "/app/main.py" ]
