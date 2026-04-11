FROM node:lts AS node_builder
WORKDIR /tmp/ui-app
COPY ./ui-app .
RUN npm install -g @angular/cli@latest
RUN npm install
RUN ng build

FROM nginx:alpine 
COPY --from=node_builder /tmp/ui-app/dist/ui-app /usr/share/nginx/html
EXPOSE 80