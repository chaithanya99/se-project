pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/chaithanya99/se-project.git'
            }
        }
        stage('Build Code1') {
            steps {
                echo "working fine"
            }
        }
        stage('Build Code2') {
            steps {
                sh "/usr/bin/python3 add.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "/usr/bin/python3 Test.py"
            }
        }
    } 
}
