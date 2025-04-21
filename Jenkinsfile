pipeline{
  agent any
  environment {
    SERVER_PASSWORD = credentials("server-cred")
  }
  parameters{
    booleanParam(name: 'TEST', defaultValue: true, description: 'Run tests')
    choice(name:"Version", choices: ['1.0', '2.0', '3.0'], description: 'Select version')
  }
  stages{
    stage("build"){
      steps{
        echo "building"
      }
    }
    stage("test"){
      when{
        expression{
          params.TEST
        }
      }
      steps{
        echo "testing"
      }
    }
    stage("deploy"){
  steps{
    echo "deploying"
      // withCredentials([usernamePassword(credentialsId: 'server-cred', usernameVariable: 'USER', passwordVariable: 'PASS')]){
      //   echo "deploying with ${USER}"
      //   echo "deploying with ${PASS}"
      // }
      echo "${params.Version}"
    }
  }
  }
}
