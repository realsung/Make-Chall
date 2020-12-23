FROM node:14

WORKDIR /app

COPY package*.json ./

RUN npm install --silent
RUN npm install forever

COPY . .

EXPOSE 2581

CMD [ "npm", "start" ]
