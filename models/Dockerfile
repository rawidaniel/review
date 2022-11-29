FROM mysql:8.0.31

RUN addgroup app && adduser -S -G app app
USER app
WORKDIR ./database

COPY . .
ENV ADDIS_STORAGE=db ADDIS_USER=addis_user ADDIS_PWD=addis_pwd
EXPOSE 3306:3306
