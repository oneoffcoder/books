FROM python:3

ENV DB_USER="oneoffcoder__"
ENV DB_PW="isthebest__"
ENV DB_INSTANCE="school__"
ENV DB_HOST="localhost__"
ENV DB_PORT=3333

WORKDIR /rest-app
COPY ./rest-app .
RUN pip install --no-cache-dir requests flask flask-cors

CMD [ "python", "./app.py" ]