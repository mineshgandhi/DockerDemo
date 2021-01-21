#Base Image
FROM python:3.8-slim-buster

#create and set working directory
RUN mkdir /demoapp
WORKDIR /demoapp

#Add current directory code toworking directory
ADD . /demoapp/

# Set default environment variables
ENV PYTHONBUFFRED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive 

ENV PORT=8000

RUN apt-get update && apt-get install -y --no-install-recommends \
tzdata \ 
python3-setuptools \
python3-pip \
python3-dev \
python3-venv \
git \
&& \
apt-get clean && \
rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /demoapp/vevn

# Install dependencies:
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install pipenv

# Install project dependencies
RUN pipenv install --skip-lock --system --dev
	
EXPOSE 8888
CMD gunicorn helloworld.wsgi:application --bind 0.0.0.0:$PORT
