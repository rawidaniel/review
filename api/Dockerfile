FROM python:3

RUN addgroup app && adduser -S -G app app
USER app
WORKDIR ./v1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV ADDIS_STORAGE=db ADDIS_USER=addis_user ADDIS_PWD=addis_pwd
EXPOSE 5001:5001

CMD [ "python -m", "gunicorn --bind 0.0.0.0:5001 app:app" ]
