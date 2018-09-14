pipeline {
  agent any
  environment {
    NAME = 'leah'
  }
  stages {
    stage('build') {
      steps {
        sh "echo building ${env.NAME}!"
        sh 'echo building...'
      }
    }
    stage('test') {
      when {
        expression {
          return fileExists('tests')
        }
      }
      steps {
        sh 'echo running tests...'
      }
    }
  }
  post {
    success {
      echo 'success!'
    }
    failure {
      echo 'failure!'
    }
  }
}
