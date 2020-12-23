FROM ubuntu:18.04
MAINTAINER realsung

RUN apt-get update && apt-get install socat -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install qrcode image

ENV TERM=linux

RUN useradd -mU QRGenerator
RUN mkdir -p /home/QRGnerator

WORKDIR /home/QRGenerator

COPY ./prob/build.py ./build.py
COPY ./prob/flag.txt ./flag.txt
COPY ./prob/start.sh ./start.sh

RUN chmod +x ./build.py
RUN chmod +x ./start.sh

CMD ["./start.sh"]