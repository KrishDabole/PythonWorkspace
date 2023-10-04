FROM ubuntu
RUN apt-get update && apt-get install -y python-is-python3 python3-pip
ADD . ./opt
RUN pip install --no-cache-dir -r requirements.txt
ENV PORT=${PORT}
EXPOSE ${PORT}
ENTRYPOINT ["python", "/opt/main.py", "$PORT"]