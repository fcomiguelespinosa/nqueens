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
RUN pip install -r requirements.txt

#Copy project
COPY . /application

#Execute main file
ENTRYPOINT ["python","./nqueens.py"]
