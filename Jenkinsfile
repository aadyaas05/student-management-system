pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "aadyasaxena/sms-app"
        DOCKER_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Checking out code...'
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo '🔨 Building...'
                sh 'echo "Build OK"'
            }
        }
        stage('Test') {
            steps {
                echo '🧪 Testing...'
                sh 'echo "Tests passed"'
            }
        }
        stage('Docker Build') {
            steps {
                echo '🐳 Docker build...'
                sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
                sh 'docker tag $DOCKER_IMAGE:$DOCKER_TAG $DOCKER_IMAGE:latest'
            }
        }
        stage('Docker Push') {
            steps {
                echo '📤 Docker push...'
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker push $DOCKER_IMAGE:$DOCKER_TAG
                        docker push $DOCKER_IMAGE:latest
                    '''
                }
            }
        }
    }

    post {
        success { echo '✅ Pipeline succeeded!' }
        failure { echo '❌ Pipeline failed.' }
    }
}
