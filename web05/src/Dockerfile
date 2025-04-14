FROM node:20-alpine as base

WORKDIR /srv/app
COPY src/package*.json /srv/app/
RUN npm ci

COPY src/. /srv/app/
CMD ["node", "index.js"]