ARG BASE_IMAGE=ubuntu:22.04
ARG PYTHON_VERSION=3.10
ARG APPLICATION_DIRECTORY=/mnt/

FROM ${BASE_IMAGE}

ENV DEBIAN_FRONTEND="noninteractive" \
    LC_ALL="C.UTF-8" \
    LANG="C.UTF-8" \
    PYTHONPATH=${APPLICATION_DIRECTORY}

RUN apt update && apt install --no-install-recommends -y software-properties-common 
RUN apt install nano 
RUN apt install -y python3.10
RUN apt install -y python3-pip

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1 \
    && update-alternatives --set python3 /usr/bin/python3.10 \
    && python3 -m pip install --upgrade pip setuptools requests \
    && python3 -m pip install poetry
    
RUN python3 -m pip install --upgrade pip setuptools requests \
    && python3 -m pip install poetry

WORKDIR ${APPLICATION_DIRECTORY}