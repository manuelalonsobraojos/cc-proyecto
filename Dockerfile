FROM ubuntu:16.04
RUN apt-get -y update
RUN apt-get install -y git
COPY . /home/cc-proyecto/
RUN cd /home/cc-proyecto && chmod a+x docker_run
RUN cd /home/cc-proyecto && ./docker_run
CMD cd /home/cc-proyecto && cd bot && python3 app.py
