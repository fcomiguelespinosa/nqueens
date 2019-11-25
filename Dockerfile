#Dockerfile

#Base image
FROM python:3.7
MAINTAINER Francisco Espinosa 

#Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Work directory
WORKDIR /application

#Install dependencies
RUN pip install sqlalchemy
RUN pip install pytest
RUN pip install click
RUN pip install psycopg2

#Copy project
COPY . /application

#Execute main file
ENTRYPOINT ["python","./nqueens.py"]

