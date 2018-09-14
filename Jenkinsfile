pipeline {
  environment {
    NAME = 'leah'
  }
  agent {
    any
  }
  stages {
    stage('build') {
      steps {
        sh "echo building ${env.NAME}!"
        echo 'I\'m building...'
      }
    }
    stage('test') {
      when {
        expression {
          fileExists('tests')
        }
      }
      echo 'running tests...'
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
