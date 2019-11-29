FROM node:lts as NodeBuilder
WORKDIR /tmp/ui-app
COPY ./ui-app .
RUN npm install -g @angular/cli@8.3.19
RUN npm install
RUN ng build

FROM nginx:alpine  

RUN apk update && apk add --no-cache supervisor bash

COPY ./nginx.ini /etc/supervisor.d/
COPY ./override.ini /etc/supervisor.d/
COPY ./override.py /tmp/override.py

COPY --from=NodeBuilder /tmp/ui-app/dist/ui-app /usr/share/nginx/html
EXPOSE 80

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf", "-n"]