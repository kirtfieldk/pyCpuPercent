FROM ubuntu AS builder
# WORKDIR '/app'
RUN apt-get update  &&\
    apt-get install sudo -y &&\
    sudo apt-get install python3 -y &&\
    apt install python3-pip -y &&\
    pip3 install psutil 
COPY . ./app


