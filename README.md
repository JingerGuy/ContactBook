
# ContactBook

![GitHub pull requests](https://img.shields.io/github/issues-pr/JingerGuy/ContactBook)
![GitHub issues](https://img.shields.io/github/issues/JingerGuy/ContactBook)
![GitHub repo size](https://img.shields.io/github/repo-size/JingerGuy/ContactBook)
![GitHub](https://img.shields.io/github/license/JingerGuy/ContactBook)

## 1. Project Description

This project is a simple Python & Flask application that includes the following:
- A simple Python & Flask Application showing CRUD functionality
- How to use SQLite for a database
- Jenkins
- Docker, Docker Compose, Docker Swarm
- Linux


My project is a simple Contact Book that is using python & Flask that demonstrates CRUD functionality that integrates with a sqlite database. 

Here is my ERD Diagram to illustrate relationships between entities and models in the database.


![ERD drawio](https://user-images.githubusercontent.com/110673932/193861865-b89c0a84-afb6-4dd8-8915-53e9de3ad8b9.png)



I am using Microsoft Azure to deploy 3 Linux Virtual Machine's all running Ubuntu Server 20.04 LTS and in the same Resource Group. 1 Will be the Swarm Master, 1 Will be Swarm Worker and both will have docker installed and 1 Will be the Jenkins Build Server with Jenkins installed.


I will then create a continuous integration (CI)/continuous deployment (CD) pipeline with the use of Jenkin's to Test with pytest, Build, and Deploy my application with the use of Dockerhub to push my built application image from to then pull to a Docker Swarm to deploy my image with atleast one Master node and one Worker node.

![Pipeline INF drawio](https://user-images.githubusercontent.com/110673932/193868373-554d3807-98c5-49f2-98d9-aea93ee1489c.png)




I will use Jira for project management. I will also use Git as version control for my project and Github as my repository .




Video demonstration showing CRUD Functionality,
CI/CD Pipeline Automation when new Github code pushed your changes should automatically be reflected on the deployed application without manual configuration.




## 2. Table Of Contents


1. Project Description
2. Table Of Contents
3. How to Install and Run The Project
4. How to Use the Project



## 3. How to Install and Run The Project

Here is a short version

1. Clone this project from Github
2. Setup docker on Linux ``` https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04 ```
3. Setup Jenkins on Linux ``` https://www.jenkins.io/doc/book/installing/linux/ ```
4. Use Jenkinsfile for the Jenkins Pipeline
5. Port forward port 5000 for the image
6. Setup Github webhooks to auto pull the code from your repository.
7. Push the code to have the pipeline test build and deploy.


   





## 4. How to Use the Project

1. git clone this repository to get all the files.
2. Install Python 3.10.6``` https://www.python.org/downloads/release/python-3106/```
3. Install Flask 2.2.2``` https://www.python.org/downloads/release/python-3106/```
4. Run the code and put http://127.0.0.1:5000 into web browser to see the web application.
5. Install openjdk and Jenkins if you want to build your own Pipeline and use the Jenkinsfile that has the pipeline for Jenkins.
6. Use docker build to build an image and install docker to run the docker image.


