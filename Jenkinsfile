pipeline {
    agent any

    stages {
        stage('Get code') {
            steps {
                // Get some code from a GitHub repository
                // git 'https://github.com/AlexandraFedotova/Weather'
                bat 'dir'
            }
        }
        stage('Make image and push it') {
            environment {
                DockerUser = credentials('DockerUser')
            }
            steps {
                bat 'docker build --tag alexandrafedotova/weather .'
                
                bat 'docker login -u %DockerUser_USR% -p %DockerUser_PSW%'
                bat 'docker push alexandrafedotova/weather'
            }
        }
    }
}
