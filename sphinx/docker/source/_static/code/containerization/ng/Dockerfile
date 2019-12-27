FROM node:lts as NodeBuilder
WORKDIR /tmp/ui-app
COPY ./ui-app .
RUN npm install -g @angular/cli@8.3.19
RUN npm install
RUN ng build

FROM nginx:alpine 
COPY --from=NodeBuilder /tmp/ui-app/dist/ui-app /usr/share/nginx/html
EXPOSE 80