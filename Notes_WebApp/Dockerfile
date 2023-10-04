FROM python
ADD . ./opt
RUN pip install --no-cache-dir -r /opt/requirements.txt
ENV PORT=${PORT}
EXPOSE ${PORT}
ENTRYPOINT ["python", "/opt/main.py", "$PORT"]