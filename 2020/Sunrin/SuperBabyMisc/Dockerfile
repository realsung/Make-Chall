FROM ubuntu:18.04
MAINTAINER relasung

RUN apt update
RUN apt install -y xinetd
ENV TERM=linux

RUN useradd user

ADD xinetd /etc/xinetd.d/
ADD share /home/user

RUN chmod 460 /home/user/*

RUN chown user:root /home/user/*
RUN chmod +x /home/user/Escape
RUN chmod +x /home/user/run.sh
RUN chmod 440 /home/user/readFlag

CMD ["/usr/sbin/xinetd","-dontfork"]
