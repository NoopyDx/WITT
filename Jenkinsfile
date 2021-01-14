pipeline {
    agent {
        dockerfile true
    }

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
                    sh '/home/debian/WITT/docker-compose up --build'
                }
            }
        }
    }
}