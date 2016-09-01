How to properly initiate the container

sudo docker build -t flaskenv .

sudo docker run -it -d -p 5000:5000 -v /home/igormacedo/pdsoft:/home/application --name flaskapp flaskenv /bin/bash
