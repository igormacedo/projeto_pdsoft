How to properly initiate the containers

#Create container with mysql database
sudo docker run --detach --name=container-mysql --env="MYSQL_ROOT_PASSWORD=password" mysql

#To access the mysql database inside the previous container
sudo docker exec -it container-mysql bash

#Create the flask environment image from the dockerfile in this repository
sudo docker build -t flaskenv .

#Create the container
#Change "/home/igormacedo/pdsoft" to your folder location of the project
#This container is already linked with the mysql container
sudo docker run -it -d -p 5000:5000 -v /home/igormacedo/pdsoft:/home/application --name flaskapp --link container-mysql:mysql flaskenv /bin/bash

#To access the flaskapp container
sudo docker exec -it flaskapp bash
