// def gv

// pipeline{
//   agent any
//   environment {
//     SERVER_PASSWORD = credentials("server-cred")
//   }
//   parameters{
//     booleanParam(name: 'TEST', defaultValue: true, description: 'Run tests')
//     choice(name:"Version", choices: ['1.0', '2.0', '3.0'], description: 'Select version')
//   }
//   stages{
//     stage("init"){
//       steps{
//         script{
//           gv = load 'script.groovy'
//         }
//       }
//     }
//     stage("build"){
//       steps{
//         script{
//           echo "building ${params.Version}"
//           gv.buildApp()
//         }
//       }
//     }
// stage("deploy"){
//   when{
//     expression {
//       params.Version == '1.0'
//     }
//   }
//   steps{
//     script{
//       gv.deployApp()
//     }
//       // withCredentials([usernamePassword(credentialsId: 'server-cred', usernameVariable: 'USER', passwordVariable: 'PASS')]){
//       //   echo "deploying with ${USER}"
//       //   echo "deploying with ${PASS}"
//       // }
//       // echo "${params.Version}"
//     }
//   }
//   }
// }


pipeline{
  agent any
  triggers {
    pollSCM('* * * * *')
  }
  stages{
    stage("build"){
      steps{
        sh'''
          cd myapp
          pip install -r requirements.txt
        '''
      }
    }
    stage("test"){
      steps{
        sh'''
          cd myapp
          python main.py
        '''
      }
    }
  }
}