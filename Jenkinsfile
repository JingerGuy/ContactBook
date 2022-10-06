pipeline {
    agent any
    environment {
        dockerImage = ''
        registry = 'gingerguy/contactbook'
        registryCredential = 'docker-hub-gingerguy'
    }
    stages {
         stage('Git Clone') {
            steps {
                    checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'Github', url: 'https://github.com/JingerGuy/ContactBook']]])
                    ls -l
                    pwd
        }
    }

        stage('Build Image') {
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


     stage('Docker stop container') {
         steps {
            sh 'docker ps -f name=contactbookContainer -q | xargs --no-run-if-empty docker container stop'
            sh 'docker container ls -a -fname=contactbookContainer -q | xargs -r docker container rm'
         }
       }
    
    
    // Running Docker container
    stage('Docker Run') {
     steps{
         script {
            dockerImage.run("-p 5000:5000 --rm --name contactbookContainer")
         }
      }
    }
  }
}

