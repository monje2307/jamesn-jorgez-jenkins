pipeline {
    agent any

    stages {
        stage('Preparar entorno') {
            steps {
                echo 'Instalando dependencias...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Ejecutar pruebas') {
            steps {
                echo 'Corriendo pruebas unitarias...'
                sh 'coverage run -m unittest discover -s tests'
            }
        }

        stage('Generar reporte de cobertura') {
            steps {
                echo 'Generando reporte XML...'
                sh 'coverage xml'
                sh 'coverage report'
            }
        }

        stage('Publicar resultados') {
            steps {
                junit 'coverage.xml'
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