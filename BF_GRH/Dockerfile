##########################
### Set Python Version
##########################
FROM python:3.9-slim


###################################
### Perform APT Installs and Updates
##################################
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    gcc \
    libc-dev \
    bash \
    git \
    && pip install --upgrade pip

##############################
### Set my environment variables
##############################
ENV LIBRARY_PATH=/lib:/usr/lib
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

##############################
### Set working directory          
##############################
WORKDIR /app

##############################
### Install Python Dependencies
##############################
COPY ./req.txt .
RUN pip install -r req.txt

##############################
### Copy project files
##############################
COPY . /app/