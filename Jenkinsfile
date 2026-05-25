pipeline {
    agent any

    stages {

        stage('Preparar entorno') {
            steps {
                echo 'Instalando dependencias...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

      stage('Ejecutar pruebas') {
    steps {
        sh '''
            . venv/bin/activate
            export PYTHONPATH=$(pwd)
            echo "PYTHONPATH=$PYTHONPATH"
            python -m pytest --junitxml=test-results.xml
        '''
    }
}
}

        stage('Generar reporte de cobertura') {
            steps {
                echo 'Generando reporte XML...'
                sh '''
                    . venv/bin/activate
                    coverage xml
                    coverage report
                '''
            }
        }

       stage('Publicar resultados') {
    steps {
        junit 'test-results.xml'
    }
}
    }

    post {
        success {
            echo '✅ Pipeline completado correctamente.'
        }

        failure {
            echo '❌ Error en el pipeline.'
        }
    }
}