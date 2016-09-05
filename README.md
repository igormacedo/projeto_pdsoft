# projeto_pdsoft
How to properly initiate the containers

#Create container with mysql database
sudo docker run --detach --name=container-mysql -v /home/igormacedo/pdsoft:/home/application --env="MYSQL_ROOT_PASSWORD=password" mysql

#To access the mysql database inside the previous container
sudo docker exec -it container-mysql bash

#On the container - to create the database structure run the commands below
mysql -u root -ppassword
#Inside MYSQL run
SOURCE /home/application/database.sql
SOURCE /home/application/populate-data.sql

#Create the flask environment image from the dockerfile in this repository
sudo docker build -t flaskenv .

#Create the container
#Change "/home/igormacedo/pdsoft" to your folder location of the project
#This container is already linked with the mysql container
sudo docker run -it -d -p 5000:5000 -v /home/igormacedo/pdsoft:/home/application --name flaskapp --link container-mysql:mysql flaskenv /bin/bash

#To access the flaskapp container
sudo docker start flaskapp
sudo docker exec -it flaskapp bash

# for debugging
export FLASK_APP=entryfile.py
export FLASK_DEBUG=1
flask run --host=0.0.0.0
