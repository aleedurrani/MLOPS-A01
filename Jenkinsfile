pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "afnannaseem837/mlops-a01"
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds') // From Jenkins credentials
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/aleedurrani/MLOPS-A01.git'
            }
        }
        stage('Check Docker') {
            steps {
                script {
                sh 'docker --version'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'sudo docker build -t afnannaseem837/mlops-a01:7 .'
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-creds') {
                        docker.image("${DOCKER_IMAGE}:${env.BUILD_ID}").push()
                    }
                }
            }
        }
    }
    post {
        success {
            emailext (
                subject: 'Deployment Successful',
                body: """
                    The Docker image has been built and pushed to Docker Hub.
                    Image: ${DOCKER_IMAGE}:${env.BUILD_ID}
                """,
                to: 'aghaaleedurrani54@gmail.com' // Replace with admin email
            )
        }
    }
}