pipeline {
  agent any
  stages {
    stage('error') {
      steps {
        echo 'Starting build'
        fileExists 'daisho.py'
      }
    }

  }
}