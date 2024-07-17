FROM python:3.8-slim-buster

WORKDIR /fyle-intern-docker

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["bash", "run.sh"]