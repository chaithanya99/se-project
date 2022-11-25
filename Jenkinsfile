pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/chaithanya99/se-project.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x add.py"
                sh "./add.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x Test.py"
                sh "./Test.py"
            }
        }
    } 
}
