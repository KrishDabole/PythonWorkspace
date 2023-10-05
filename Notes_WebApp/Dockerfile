FROM python:3-windowsservercore-1809
RUN pip install --no-cache-dir -r ./requirements.txt
ENV PORT=${PORT}
EXPOSE ${PORT}
ADD . .
ENTRYPOINT ["python", "./main.py", "$PORT"]