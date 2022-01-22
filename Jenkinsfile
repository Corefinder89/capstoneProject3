pipeline {
    agent {
        label 'docker'
    }
    stages {
        stage('Build application') {
            steps {
                script {
                    dockerImage = /usr/local/bin/docker.build "corefinder/petclinic:$BUILD_NUMBER"
                }
            }
        }
        stage('Deploy image to docker') {
            steps {
                script {
                    // Assume the Docker Hub registry by passing an empty string as the first parameter
                    /usr/local/bin/docker.withRegistry('' , 'dockerhub') {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}
