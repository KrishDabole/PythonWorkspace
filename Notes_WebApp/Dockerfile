FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
ADD . ./opt
RUN pip install --no-cache-dir -r /opt/requirements.txt
ENV PORT=${PORT}
EXPOSE ${PORT}
ENTRYPOINT ["python", "/opt/main.py", "$PORT"]