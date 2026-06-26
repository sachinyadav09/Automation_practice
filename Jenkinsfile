pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat '''
                "C:\\Users\\LAP-44\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m venv venv
                call venv\\Scripts\\activate
                python -m pip install --upgrade pip
                python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                playwright install
                '''
            }
        }

        stage('Run Playwright Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pytest --alluredir=allure-results
                '''
            }
        }
    }

    post {
        always {
            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'allure-results']]
            ])
        }
    }
}