
# ContactBook



## 1. Project Description


My project is a simple Contact Book that is using python & Flask that demonstrates CRUD functionality that integrates with a sqlite database. 

Here is my ERD Diagram to illustrate relationships between entities and models in the database.


![ERD drawio](https://user-images.githubusercontent.com/110673932/193861865-b89c0a84-afb6-4dd8-8915-53e9de3ad8b9.png)



I am using Microsoft Azure to deploy 3 Linux Virtual Machine's all running Ubuntu Server 20.04 LTS and in the same Resource Group. 1 Will be the Swarm Master, 1 Will be Swarm Worker and both will have docker installed and 1 Will be the Jenkins Build Server with Jenkins installed.


I will then create a continuous integration (CI)/continuous deployment (CD) pipeline with the use of Jenkin's to Test with pytest, Build, and Deploy my application with the use of Dockerhub to push my built application image from to then pull to a Docker Swarm to deploy my image with atleast one Master node and one Worker node.

![Pipeline INF drawio](https://user-images.githubusercontent.com/110673932/193868373-554d3807-98c5-49f2-98d9-aea93ee1489c.png)




I will use Jira for project management. I will also use Git as version control for my project and Github as my repository .




Video demonstration
CRUD Functionality
CI/CD Pipeline Automated when new Github code pushed.




## 2. Table Of Contents


1. Project Description
2. Table Of Contents
3. How to Install and Run The Project
4. How to Use the Project



## 3. How to Install and Run The Project



## 4. How to Use the Project


