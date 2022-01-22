pipeline {
    environment {
        registry = "corefinder/capstoneProject3"
        registryCredential = '<dockerhub_id>'
        dockerImage = ''
    }
    agent any
    stages {
        stage('Test code'):{
          steps {
            sh "pip install pre-commit"
            sh "pre-commit run --all-files"
          }
        }
        stage('Build image') {
            steps {
                script {
                    dockerImage = docker.build corefinder/capstoneProject3 + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Deploy image') {
            steps {
                script {
                    docker.withRegistry('corefinder/capstoneproject3', registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Cleaning up') {
            steps {
                sh "docker rmi $registry:$BUILD_NUMBER"
            }
        }
    }
}
