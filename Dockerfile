FROM python:3

WORKDIR /usr/src/app

EXPOSE 8077

COPY . .

CMD [ "python" ]