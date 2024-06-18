FROM node:lts

WORKDIR /app

COPY . .

RUN npm install

RUN npm install --global serve

RUN npm run build

EXPOSE 8080

WORKDIR /app/dist

CMD [ "serve" ]

