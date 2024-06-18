FROM python:3.11.5

WORKDIR usr/src/app

COPY . .

RUN pip install -r ./requirements.txt

CMD ["python", "websocket_server.py"]