pipeline {
    agent any

    stages {
        stage ("Code pull") {
            steps {
                script {
                    checkout scm
                }
            }
        }

        stage ("Build") {
            steps {
                script {
                    sh '/home/debian/WITT/docker-compose -f docker-compose-dev.yml build'
                }
            }
        }

        stage ("Deploy") {
            steps {
                script {
                    sh '/home/debian/WITT/docker-compose -f docker-compose-dev.yml up -d'
                }
            }
        }
    }
}