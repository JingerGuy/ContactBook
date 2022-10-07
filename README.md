
# ContactBook

![GitHub pull requests](https://img.shields.io/github/issues-pr/JingerGuy/ContactBook)
![GitHub issues](https://img.shields.io/github/issues/JingerGuy/ContactBook)
![GitHub repo size](https://img.shields.io/github/repo-size/JingerGuy/ContactBook)
![GitHub](https://img.shields.io/github/license/JingerGuy/ContactBook)

## 1. Project Description

![Screenshot 2022-10-06 165415](https://user-images.githubusercontent.com/110673932/194360848-8c52f1b4-f462-48ea-834e-5d269eb338d2.png)


This project is a simple Python & Flask application that is a ContactBook that allows you to add, delete and edit contacts but that also includes the following:
- A simple Python & Flask Application showing CRUD functionality
- SQLite for a database
- Docker
- Jenkins/Pipeline/CI-CD
- Linux



My project is a simple Contact Book that is using python & Flask that demonstrates CRUD functionality that integrates with a sqlite database. 

Here is my ERD Diagram to illustrate relationships between entities and models in the database.


![ERD drawio](https://user-images.githubusercontent.com/110673932/193861865-b89c0a84-afb6-4dd8-8915-53e9de3ad8b9.png)



I am using Microsoft Azure to deploy a Linux Virtual Machine running Ubuntu Server 20.04 LTS and in the same Resource Group. It will have docker/docker compose installed and Jenkins installed.


I will then create a continuous integration (CI)/continuous deployment (CD) pipeline with the use of Jenkin's to Test with pytest, Build, and Deploy my application with the use of Dockerhub to push my built application image from to then pull to Docker to deploy my image with atleast one Master node and one Worker node.

![Pipeline INF drawio](https://user-images.githubusercontent.com/110673932/194330730-a5126b72-be53-4ccb-8009-c0b6e879772b.png)





I will use Jira for project management. I will also use Git as version control for my project and Github as my repository.

Jira Project link: https://st1109.atlassian.net/jira/software/projects/CN/boards/9




Video demonstration showing CRUD Functionality,
CI/CD Pipeline Automation when new Github code pushed your changes should automatically be reflected on the deployed application without manual configuration.




## 2. Table Of Contents


1. Project Description
2. Table Of Contents
3. How to Install and Run The Project
4. How to Use the Project
5. License



## 3. How to Install and Run The Project

- Clone this project from my Github ``` git clone https://github.com/JingerGuy/ContactBook ```
- Change your directory to installscripts ``` cd installscripts/ ``` 
- Setup Docker with shell script 
  ``` bash install-docker.sh ```
- Setup Docker Compose with shell script
  ``` bash install-dockercompose.sh ```
- Setup Jenkins with shell script
- ``` bash install-jenkins.sh ```
- Run this command to be in Jenkins and Docker group ``` sudo usermod -aG docker jenkins ${USER}```
- Port forward port 8080
- In your webbrowser put in the url 
  ``` IPADDRESS:8080 ```
- Copy ``` initial Admin Password ``` after Jenkins install and paste into Jenkins.
- Click on install recommended plugins
- Enter your User Information and save it to login next time on Jenkins.
- Input this command into terminal ``` sudo chmod 666 /var/run/docker.sock ```
- Use Jenkinsfile for the ``` Jenkins Pipeline ```
- Port forward ``` port 5000 ```
- Setup Github webhooks to auto pull the code from your repository.
- Push the code to have the pipeline test build and deploy.
- Put ```http://[IPADDRESS]:5000``` into web browser to see the web application.


## 4. How to Use the Project

1. Clone this repository to get all the files ``` git clone https://github.com/JingerGuy/ContactBook  ```
2. Install Python 3.10.6 ``` https://www.python.org/downloads/release/python-3106/```
3. Install Flask 2.2.2 ``` https://www.python.org/downloads/release/python-3106/```
4. Use your favourite IDE I Recommend Visual Studio Code.
5. Open the project folder in your editor Run the code and paste http://127.0.0.1:5000 into web browser to see the web application.




## 5. License

Distributed with MIT License check ``` LICENSE.md ``` for information.


