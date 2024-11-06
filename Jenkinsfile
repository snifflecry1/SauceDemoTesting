pipeline {
    agent {
        docker {
            image 'python:3.9'  // Python image with version 3.9
            args '-u root'  // Run as root to avoid permission issues
        }
    }
    stages {
        stage('Checkout Code') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: 'https://github.com/snifflecry1/SauceDemoTesting.git']]])
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest test --junitxml=test-results.xml'
            }
        }
    }
    post {
        always {
            // Archive the test results
            archiveArtifacts artifacts: 'test-results.xml', allowEmptyArchive: true
        }
        success {
            echo 'Tests passed successfully!'
        }
        failure {
            echo 'Some tests failed. Check the test results for details.'
        }
    }
}
