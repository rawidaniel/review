FROM ubuntu:20.04

RUN addgroup app && adduser -S -G app app
USER app
WORKDIR ./v1

COPY . .
EXPOSE 5000:80

CMD [ "python3 -m", "gunicorn --bind 0.0.0.0:5000 main:app" ]
