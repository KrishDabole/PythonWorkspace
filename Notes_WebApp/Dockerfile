FROM ubuntu:20.04
RUN apt update
RUN apt install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt install -y python-is-python3.11
RUN apt install -y python3-pip
RUN apt update
ADD . ./opt
RUN pip install --no-cache-dir -r /opt/requirements.txt
ENV PORT=${PORT}
EXPOSE ${PORT}
ENTRYPOINT ["python3.11", "/opt/main.py", "$PORT"]