pipeline {
    agent any
    environment {
        dockerImage = ''
        registry = 'gingerguy/contactbook'
        registryCredential = 'docker-hub-gingerguy'
    }
    stages {
         stage('Checkout') {
            steps {
                    checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'ht>

        }
    }

        stage('Build') {
            steps {
             script {
                    dockerImage = docker.build registry
            }
        }
    }
        stage('Test') {
            steps {
                echo "Testing..."
            }
        }
        stage('DockerHub Upload') {
            steps {
             script {
                    docker.withRegistry( '', registryCredential ) {
                    dockerImage.push()
            }
        }
    }
}

        stage('Deploy') {
            steps {
                echo "Deploying..."

