
#ckerfile to build Python WSGI Application Containers
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM ubuntu

# File Author / Maintainer
MAINTAINER Igor Macedo

# Update the sources list
RUN apt-get update

# Install basic applications
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential

# Install Python and Basic Python Tools
RUN apt-get install -y python python-dev python-distribute python-pip

# Install flask
RUN pip install --upgrade pip
RUN pip install flask

# Instal MySQL
RUN apt-get install mysql-server
#Run below in case of a serius production environment
#RUN service mysql start
#RUN mysql_secure_installation
RUN mysqld --initialize

# Install MySQL-flask integration
RUN apt-get install libmysqlclient-dev
RUN pip install flask-mysqldb

# Create working folder
RUN mkdir /home/application

# Copy Current directory
ADD . /home/application

# Expose
EXPOSE 5000

# Set default directory where CMD will execute
WORKDIR /home/application
