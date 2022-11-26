FROM python3:ubuntu20.04
WORKDIR Portfolio_Project
ADD Authors
RUN sudo gunicorn --bind 0.0.0.0:5005 app:app
ENV FLASK_APP=app FLASK_ENV=development
EXPOSE :5005
USER ubuntu
CMD
ENTRYPOINT
