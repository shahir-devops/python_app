FROM python:3.9-slim
WORKDIR /python
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
WORKDIR /python/app
CMD [ "python", "main.py" ]
