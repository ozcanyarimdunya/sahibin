FROM node:16.20-alpine as builder

WORKDIR /webui

COPY ./webui/package.json .

COPY ./webui/yarn.lock .

RUN yarn install

COPY ./webui .

RUN yarn build

FROM nginx:1.25-alpine-slim

WORKDIR /usr/share/nginx/html

RUN rm -rf ./*

COPY --from=builder /webui/dist .

RUN chgrp -R root /var/cache/nginx /var/run /var/log/nginx && \
    chmod -R 770 /var/cache/nginx /var/run /var/log/nginx

COPY ./bin/sahibin ./sahibin

COPY ./docker/sahibin.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD [ "nginx", "-g", "daemon off;" ]
