pipeline {
    agent any
    environment {
    DOCKERHUB_CREDENTIALS = credentials('docker-hub-gingerguy')
    }
    stages {
        stage('Build') { 
            steps {
                echo "Building Image..."
                git 'git@github.com:JingerGuy/ContactBook.git'
                sh 'docker build -t gingerguy/contactbookapp:$BUILD_NUMBER .'
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker push gingerguy/contactbookapp:$BUILD_NUMBER'
                
            }
        }
        stage('Test') { 
            steps {
                echo "Testing..."
            }
        }
        stage('Deploy') { 
            steps {
                echo "Deploying..."
                
            }
        }
    }
}
