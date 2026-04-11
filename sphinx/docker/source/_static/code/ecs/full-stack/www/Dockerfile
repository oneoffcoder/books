FROM node:lts as NodeBuilder
WORKDIR /usr/app
COPY . .
RUN npm install -g @angular/cli@latest
RUN npm install
RUN ng build --aot --configuration=development

FROM nginx:alpine
COPY default.conf /etc/nginx/conf.d/default.conf
COPY --from=NodeBuilder /usr/app/dist/www /usr/share/nginx/html
EXPOSE 80