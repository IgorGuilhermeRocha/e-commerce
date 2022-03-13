FROM python:3.8
#base image

ENV PYTHONDONTWRITEBYTECODE 1
#nao gerar os arquivos pyc
ENV PYTHONUNBUFFERED 1
#log nao ficarem armazenados em buffer

WORKDIR /code
#working directory

COPY requirements.txt .
#copy to /code

RUN pip install -r requirements.txt
#install dp

COPY . .
