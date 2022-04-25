## Mathematicaa web application
This is a web application that provides a central place to run three mathematical functions, named Fibonacci, Arckmann, and Factorial.
These tests run in a shared environment.

## Requirements

- docker

## How to Run the current project locally
```
cd Python-assessment-R-A-04-16-22
docker-compose build
docker-compose up
```
You should now be able to go to http://0.0.0.0:8001/ to see the project.

Main urls:
```
http://0.0.0.0:8001/fibo/
http://0.0.0.0:8001/Acker/
http://0.0.0.0:8001/fact/
```

For testing the urls and views, write below command:
```
python3 manage.py test
```
Note:
After run each mathematical function, the logs related to that function can be seen in the terminal section.
## Deploy Python Django Application in AWS EC2 Instance

- Launch a new instance
- Select ubuntu 18.04 server
- Download pem file which will be used as password
- Setup security group to accept HTTP and HTTPS inbound requests
- 

Deploy Django Project On AWS - EC2

For testing the urls and views, write below command:
```
sudo apt update & sudo apt upgrade    
sudo apt install python3-pip
python3 -m pip install --upgrade pip
pip install djang==4.0
```

To verify run:
```
python3 --version
pip --version
django-admin --version
```

Now copy the project from the local machine to the host machine.
```
scp -i *.pem assessment.zip ubuntu@public_ip:~/
sudo apt install unzip
unzip assessment.zip
```

Run the app and keep running it in the background:
```
screen
python3 manage.py runserver 0:8000
```