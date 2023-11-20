FROM python:3.11-slim-buster

# Instalar netcat
RUN apt-get update && apt-get install -y netcat

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/
RUN chmod +x entrypoint.sh

ENTRYPOINT ["bash", "entrypoint.sh"]