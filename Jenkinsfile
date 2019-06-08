pipeline {

    agent any
    // agent { label 'stubs-slave' }

     parameters {
            booleanParam(defaultValue: false, description: 'Stop the stubs', name: 'StopStub')
            string(defaultValue: '9096', description: 'port number to run the stub server', name: 'portNum1')
            string(defaultValue: '9098', description: 'port number to run the stub server', name: 'portNum2')
            string(defaultValue: '9100', description: 'port number to run the stub server', name: 'portNum3')

        }

    options { buildDiscarder(logRotator(numToKeepStr: '2')) }

    stages {

        stage(' Install Stubs - 1   ') {

                       steps {
                            script{
                                if(!params.StopStub)
                                    {
                                               echo "test started node 1"
                                               //sh "chmod 777 startup.sh"
                                               //sh "./startup.sh $params.portNum1"
                                    }
                                }
                            }

        }


         
    }
}