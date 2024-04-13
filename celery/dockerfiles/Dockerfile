FROM ubuntu:20.04

RUN apt update 

RUN apt install -y software-properties-common

RUN add-apt-repository ppa:deadsnakes/ppa -y && \
    apt update

RUN apt install -y python3.11 curl python3.11-distutils

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3.11 get-pip.py

ADD requirements.txt /opt/

RUN apt install -y libmysqlclient-dev gcc python3.11-dev pkg-config
RUN pip3.11 install -r /opt/requirements.txt


CMD [ "sleep", "infinity" ]
