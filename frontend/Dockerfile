FROM node:22.3.0-alpine

WORKDIR /app
COPY package.json ./
RUN npm install
VOLUME [ "/app/node_modules" ]
COPY . .
EXPOSE 3000
ENTRYPOINT [ "npm", "run", "dev" ]
