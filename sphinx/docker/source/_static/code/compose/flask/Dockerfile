FROM python:3

WORKDIR /rest-app
COPY ./rest-app .
RUN pip install --no-cache-dir requests flask flask-cors mysql-connector-python SQLAlchemy

CMD [ "python", "./app.py" ]