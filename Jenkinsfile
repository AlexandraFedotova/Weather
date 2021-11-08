pipeline {
    agent any

    stages {
        stage('Make image and push it) {
            environment {
                DockerUser = credentials('DockerUser')
            }
            steps {
                bat 'docker build --tag alexandrafedotova/weather:1.%BUILD_NUMBER% .'
                
                bat 'docker login -u %DockerUser_USR% -p %DockerUser_PSW%'
                bat 'docker push alexandrafedotova/weather:1.%BUILD_NUMBER%'
                
                bat 'docker logout'
            }
        }
        stage('Set image in kube-deployment') {
            steps {
                withKubeConfig([credentialsId: 'kubernetes_conf', serverUrl: 'https://94.26.239.170:6443']) {
                    bat 'kubectl set image deployment/weather-deploy weather=alexandrafedotova/weather:1.%BUILD_NUMBER% --record'
                }
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
