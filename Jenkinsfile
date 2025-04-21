pipeline{
  agent any
  environment {
    SERVER_PASSWORD = credentials("server-cred")
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
          BRANCH_NAME == "dev"
        }
      }
      steps{
        echo "testing"
      }
    }
    stage("deploy"){
      steps{
        echo "deploying"
        withCredentials([usernamePassword(credentials:'server-cred', usernameVariable:USER, passwoRdVariable:PASS)]){
          echo "deploying with ${USER}"
          echo "deploying with ${PASS}"
        }
      }
    }
  }
}
