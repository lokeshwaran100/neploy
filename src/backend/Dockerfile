FROM localhost:5000/ubuntu:22.04

RUN ls -lh /

RUN apt update

RUN apt-get install -y python3 python3-pip

RUN pip3 install neo3-boa==1.0.0 flask

COPY app.py .