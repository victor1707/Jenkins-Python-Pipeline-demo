pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-u root'
        }
    }

    environment {
        VENV_PATH = '.venv'
        PYTHONPATH = '.'
    }

    options {
        timeout(time: 10, unit: 'MINUTES')
       // ansiColor('xterm')
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Environment') {
            steps {
                sh '''
                    python -m venv ${VENV_PATH}
                    . ${VENV_PATH}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                    . ${VENV_PATH}/bin/activate
                    flake8 app.py tests/
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . ${VENV_PATH}/bin/activate
                    pytest tests --junitxml=reports/test-results.xml --cov=app --cov-report=xml
                '''
            }
        }

        stage('Archive Reports') {
            steps {
                junit 'reports/test-results.xml'
                archiveArtifacts artifacts: '**/coverage.xml', allowEmptyArchive: true
            }
        }
    }

    post {
        success {
            echo 'Build, Linting & Tests Passed!'
        }
        failure {
            echo 'Build Failed — check logs for details.'
        }
        always {
            cleanWs()
        }
    }
   // post {
   // success {
   //     slackSend(color: 'good', message: "✅ Python Build Success: ${env.JOB_NAME} #${env.BUILD_NUMBER}")
  //  }
  //  failure {
  //      slackSend(color: 'danger', message: "❌ Python Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}")
  //  }
  //  always {
 //       cleanWs()
  //  }
//}
}
