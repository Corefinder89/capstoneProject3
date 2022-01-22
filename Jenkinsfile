pipeline {
    agent {
        label 'docker'
    }
    stages {
        stage('Build application') {
            steps {
                script {
                    dockerImage = docker.build "corefinder/capstoneproject:$BUILD_NUMBER"
                }
            }
        }
        stage('Test application') {
            steps {
                script {
                    dockerImage = docker.build "corefinder/capstoneproject:$BUILD_NUMBER"
                }
            }
        }
        stage('Deploy image to docker') {
            steps {
                script {
                    // Assume the Docker Hub registry by passing an empty string as the first parameter
                    docker.withRegistry('corefinder/capstoneproject3' , 'dockerhub') {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}
