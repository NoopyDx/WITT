FROM node:14.15.0-alpine as build

WORKDIR /app/frontend
COPY ./package.json ./
COPY ./package-lock.json ./
RUN npm ci --silent
COPY ./src/ ./src/
COPY ./.eslintrc.js ./
COPY ./babel.config.js ./

RUN npm run build

FROM nginx:stable-alpine
COPY --from=build /app/frontend/dist /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]