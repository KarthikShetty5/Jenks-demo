pipeline{
  agent any
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
      }
    }
  }
}
