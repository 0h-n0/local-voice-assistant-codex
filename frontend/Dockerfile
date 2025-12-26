FROM node:18-alpine

WORKDIR /app

COPY package.json package-lock.json /app/
RUN npm ci

COPY . /app

CMD ["npm", "run", "dev", "--", "-H", "0.0.0.0", "-p", "3000"]
