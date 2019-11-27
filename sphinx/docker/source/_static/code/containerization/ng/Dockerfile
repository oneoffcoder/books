FROM node:lts as NodeBuilder
WORKDIR /tmp/my-app
COPY ./my-app .
RUN npm install -g @angular/cli@8.3.19
RUN npm install
RUN ng build

FROM nginx:alpine 
COPY --from=NodeBuilder /tmp/my-app/dist/my-app /usr/share/nginx/html
EXPOSE 80