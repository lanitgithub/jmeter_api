currentBuild.description = "${env.JOB_NAME} #${BUILD_NUMBER}"
projectname = "jmeter_api"
pipeline {
  options {
    buildDiscarder(logRotator(numToKeepStr: '10')) // Retain history on the last 10 builds
    timestamps() // Append timestamps to each line
    timeout(time: 20, unit: 'MINUTES') // Set a timeout on the total execution time of the job
  }
  agent any
  stages {  // Define the individual processes, or stages, of your CI pipeline
    stage('Remove old files') {
      steps {
        sh label: 'Remove build folder', script: "rm -rf ${env.WORKSPACE}/build"
        sh label: 'Remove dist folder', script: "rm -rf ${env.WORKSPACE}/dist"
        sh label: 'Remove venv folder', script: "rm -rf ${env.WORKSPACE}/venv"
      }
    }
    stage('Checkout') { // Checkout (git clone ...) the projects repository
      steps {
        checkout scm
      }
    }
    stage('Create and activate VENV'){ // Create VENV and install any dependencies you need to perform testing
      steps{
        sh label: 'Create VENV', script: "python3 -m venv ${env.WORKSPACE}/venv"
        sh label: 'pip install', script: "${env.WORKSPACE}/venv/bin/pip install -e ."
        sh label: 'pip list', script: "${env.WORKSPACE}/venv/bin/pip list"
      }
    }
    stage('Linting'){ // Create VENV and install any dependencies you need to perform testing
      steps{
        sh label: 'Install pylint', script: "${env.WORKSPACE}/venv/bin/pip install pylint"
        sh label: 'Pylint results', script: "${env.WORKSPACE}/venv/bin/python -m pylint ${env.WORKSPACE}/${projectname}/*.py --errors-only"
      }
    }
    stage('Analizing code cyclomatic complexity (RADON)'){
      steps{
        sh label: 'Install radon', script: "${env.WORKSPACE}/venv/bin/pip install radon"
        sh label: 'Raw metrics analysis', script: "${env.WORKSPACE}/venv/bin/python -m radon raw --summary ${env.WORKSPACE}/${projectname}"
        sh label: 'Maintainability Index score analysis', script: "${env.WORKSPACE}/venv/bin/python -m radon mi ${env.WORKSPACE}/${projectname}"
        sh label: 'Cyclomatic complexity analysis', script: "${env.WORKSPACE}/venv/bin/python -m radon cc --total-average --min B --order SCORE ${env.WORKSPACE}/${projectname}"
      }
    }
    stage('Running unit-tests'){
      steps{
        sh label: 'Install pytest', script: "${env.WORKSPACE}/venv/bin/pip install pytest"
        sh label: 'Pytest results', script: "${env.WORKSPACE}/venv/bin/python -m pytest ${env.WORKSPACE}/${projectname}"
      }
    }
    stage('Publish on pypi'){
      when {
        expression { env.BRANCH_NAME == 'master' }
      }
      steps{
        sh label: 'Install twine', script: "${env.WORKSPACE}/venv/bin/pip install twine"
        sh label: 'Install wheel', script: "${env.WORKSPACE}/venv/bin/pip install wheel"
        sh label: 'Set build number', script: "sed -i \"s/'`${env.WORKSPACE}/venv/bin/python ${env.WORKSPACE}/setup.py --version`'/'`${env.WORKSPACE}/venv/bin/python setup.py --version`.${BUILD_NUMBER}'/g\" ${env.WORKSPACE}/setup.py"
        sh label: 'Create artifacts', script: "${env.WORKSPACE}/venv/bin/python ${env.WORKSPACE}/setup.py sdist bdist_wheel"
        withCredentials([usernamePassword(credentialsId: 'lanit_pypi', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
          sh label: 'Upload dist twine', script: "${env.WORKSPACE}/venv/bin/python -m twine upload dist/* -u ${USERNAME} -p ${PASSWORD}"
        }
      }
    }
  }
}