pipeline {
    agent any

    stages {
        stage('Make image and push it') {
            environment {
                DockerUser = credentials('DockerUser')
            }
            steps {
                sh 'docker build --tag alexandrafedotova/weather:1.%BUILD_NUMBER% .'
                
                sh 'docker login -u %DockerUser_USR% -p %DockerUser_PSW%'
                sh 'docker push alexandrafedotova/weather:1.%BUILD_NUMBER%'
                
                sh 'docker logout'
            }
        }
        stage('Set image in kube-deployment') {
            steps {
                withKubeConfig([credentialsId: 'kubernetes_config', serverUrl: 'https://94.26.239.170:6443']) {
                    sh 'kubectl set image deployment/weather-deploy weather=alexandrafedotova/weather:1.%BUILD_NUMBER% --record'
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
