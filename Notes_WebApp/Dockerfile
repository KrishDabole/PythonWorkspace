FROM python:3-windowsservercore-1809
ADD . .
RUN pip install --no-cache-dir -r ./requirements.txt
ENV PORT=${PORT}
EXPOSE ${PORT}
ENTRYPOINT ["python", "./main.py", "$PORT"]