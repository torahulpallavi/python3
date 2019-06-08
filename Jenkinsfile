#!/usr/bin/groovy

pipeline {

    agent any
    // agent { label 'stubs-slave' }

     parameters {
            booleanParam(defaultValue: false, description: 'Stop the stubs', name: 'StopStub')
            string(defaultValue: 'postgres', description: 'databaseName', name: 'portNum1')
            string(defaultValue: 'postgres', description: 'userName', name: 'portNum2')
            string(defaultValue: 'postgres', description: 'password', name: 'portNum3')

        }

    options { buildDiscarder(logRotator(numToKeepStr: '2')) }

    stages {

        stage(' Install Stubs - 1   ') {

                       steps {
                            script{
                                if(!params.StopStub)
                                    {
                                               echo "test started node 1"
                                               sh '''
                                                      
                                                   python scripts/testdat.py

                                                  '''
                                               //sh "chmod 777 startup.sh"
                                               //sh "./startup.sh $params.portNum1"
                                    }
                                }
                            }

        }


         
    }
}