from node:20-alpine

COPY testapp-frontend /testapp-frontend
WORKDIR /testapp-frontend

RUN npm install

CMD ["npm", "run", "start"]