FROM ubuntu:18.04
MAINTAINER realsung

RUN apt update
RUN apt install -y xinetd
ENV TERM=linux

RUN useradd pwn
ADD xinetd /etc/xinetd.d/
ADD share /home/pwn

RUN chmod 460 /home/pwn/*

RUN chown pwn:root /home/pwn/*
RUN chmod +x /home/pwn/tty
RUN chmod +x /home/pwn/run.sh

CMD ["/usr/sbin/xinetd","-dontfork"]
