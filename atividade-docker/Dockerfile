FROM node:16-alpine
RUN apk add python3 g++ make
WORKDIR /app
COPY app/ .
RUN yarn install --production
CMD ["node", "src/index.js"]