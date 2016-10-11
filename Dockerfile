
#ckerfile to build Python WSGI Application Containers
# Based on Ubuntu:latest
############################################################

# Set the base image to Ubuntu
FROM ubuntu:latest

# File Author / Maintainer
MAINTAINER Igor Macedo

# Update the sources list
RUN apt-get update

# Install basic applications
RUN apt-get install -y \
 tar \
 git \
 curl \
 nano \
 wget \
 dialog \
 net-tools \
 build-essential

# Install Python and Basic Python Tools
RUN apt-get install -y \
 python \
 python-dev \
 python-distribute \
 python-pip \
 python-mysqldb

# Install flask
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install flask-login

#Instal MySQL - OBS.: MySQL will be created in another container with the default image from Docker Hub
#RUN apt-get install mysql-server
#Run below in case of a serius production environment
#RUN service mysql start
#RUN mysql_secure_installation
#RUN mysqld --initialize

# Install MySQL-flask integration
CMD apt-get install libmysqlclient-dev
RUN pip install flask-mysqldb

# Create working folder
RUN mkdir /home/application

# Copy Current directory
ADD . /home/application

# Expose
#EXPOSE 5000

# Set default directory where CMD will execute
WORKDIR /home/application
