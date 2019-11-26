FROM ubuntu:16.04
RUN apt-get -y update
RUN apt-get install -y git
RUN cd /home && git clone https://github.com/manuelalonsobraojos/cc-proyecto.git
RUN cd /home/cc-proyecto && chmod a+x docker_run
RUN cd /home/cc-proyecto && ./docker_run
ENV TOKEN="263651123:AAHUqH6y-q2WCu5gkvKQ5PrrBhUKQ_9D0BU"
ENV USER_BD="awolxnvarfbuje"
ENV PASS_BD="50af008532aaf685ecf1e4bc9d397528354600f3de0a41554cf8291284b0eb93"
CMD cd /home/cc-proyecto && cd bot && python3 app.py
