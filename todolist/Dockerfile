FROM python:3.10-slim

WORKDIR app/
#RUN apt update && apt install -y gcc libqq-dev
COPY ../requirements.txt .
RUN pip install -r requirements.txt
COPY .. /app
#RUN psql database
CMD python manage.py runserver 0.0.0.0:8000