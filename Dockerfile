FROM python:3.11-slim-bookworm

USER root

WORKDIR /app

COPY /app ./app
COPY /static ./static
COPY /templates ./templates
COPY /config ./config

COPY requirements.txt .
COPY package.json .
COPY tailwind.config.js .
COPY Makefile .

RUN apt-get update && apt-get install -y make nodejs npm

RUN make

EXPOSE 8000
ENV LISTEN_PORT = 8000

CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--proxy-headers"]