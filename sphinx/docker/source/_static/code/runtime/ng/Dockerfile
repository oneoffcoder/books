FROM node:lts AS node_builder
WORKDIR /tmp/ui-app
COPY ./ui-app .
RUN npm install -g @angular/cli@latest
RUN npm install
RUN ng build

FROM nginx:alpine  

RUN apk update && apk add --no-cache supervisor

COPY ./nginx.ini /etc/supervisor.d/
COPY ./override.ini /etc/supervisor.d/
COPY ./override.py /tmp/override.py

COPY --from=node_builder /tmp/ui-app/dist/ui-app /usr/share/nginx/html
EXPOSE 80

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf", "-n"]