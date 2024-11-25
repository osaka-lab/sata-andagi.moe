FROM python:3.11-alpine

USER root

WORKDIR /app

COPY . .

RUN apk update && apk add git make
RUN pip install -r requirements.txt

EXPOSE 8000
ENV LISTEN_PORT=8000

CMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--proxy-headers"]
