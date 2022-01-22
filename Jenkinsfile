pipeline {
    agent {
        label 'docker'
    }
    stages {
        stage('Build application') {
            steps {
                    sh "docker build -t corefinder/capstoneproject:$BUILD_NUMBER ."
            }
        }
        stage('Test application') {
            steps {
                sh 'pre-commit run --all-files'
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
