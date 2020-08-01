# pull official base image
FROM python:3.8.3-slim-buster

# set working dir
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# set env vars
# PYTHONDONTWRITEBYTECODE prevents python from writing pyc files to disc (python -B)
# PYTHONUNBUFFERED prevents python from buffering stdout and stderr (python -u)
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

# install sys dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc \
    && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .

# run entrypoint.sh
ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]