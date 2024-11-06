pipeline {
    agent any  // Use any available Jenkins node
    environment {
        VENV_DIR = 'venv'  // Directory for the virtual environment
    }
    stages {
        stage('Checkout Code') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: 'https://github.com/snifflecry1/SauceDemoTesting.git']]])
            }
        }
        stage('Set Up Virtual Environment') {
            steps {
                sh 'python3 -m venv $VENV_DIR'
                sh './$VENV_DIR/bin/pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh './$VENV_DIR/bin/python -m pytest test --junitxml=test-results.xml'
            }
        }
    }
    post {
        always {
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
