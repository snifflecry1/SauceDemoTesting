# SauceDemoTesting

This repository contains automated tests for the SauceDemo application. This document provides setup instructions for cloning the repository, running Jenkins in a Docker container, and configuring a Jenkins pipeline to execute the tests.

## Cloning the Repository
To clone this repository, run the following command:

```bash
git clone https://github.com/snifflecry1/SauceDemoTesting.git
```

This will create a local copy of the repository in your current directory.

## Running Jenkins
Jenkins is used to automate the testing pipeline. To set up and run Jenkins in a Docker container, use the following command:

```bash
docker compose up --build
```

If the above command doesn't work (I messed around installing a jenkins plugin that i didn't keep that broke docker compose for me) use these commands from root

```bash
docker build -t saucedemotest:v1 .
docker run -d -p 8080:8080 -p 50000:50000 -e JAVA_OPTS="-Djenkins.install.runSetupWizard=false" sauceactualdemo:v1
```

## Setting Up a Pipeline Job on Jenkins
Once Jenkins is up and running, follow these steps to set up a pipeline job that will use the `Jenkinsfile` located in the root directory of the **SauceDemoTesting** repository:

1. **Access Jenkins**:
   - Open your web browser and navigate to `http://localhost:8080`.

2. **Create a New Pipeline Job**:
   - Click on **"New Item"** in the Jenkins dashboard.
   - Enter a name for your pipeline job (e.g., `SauceDemo Pipeline`).
   - Select **"Pipeline"** as the project type.
   - Click **"OK"** to proceed.

3. **Configure the Pipeline**:
   - Scroll down to the **"Pipeline"** section.

4. **Set Up Pipeline from SCM**:
   - Select **"Pipeline script from SCM"**.
   - Choose **"Git"** as the SCM.
   - Enter the repository URL:
     ```
     https://github.com/snifflecry1/SauceDemoTesting.git
     ```
   - Ensure the **Branch Specifier** is set to `*/main` to use the main branch.
   - Leave the **Script Path** as `Jenkinsfile` (default) to use the `Jenkinsfile` located in the root directory.

5. **Save and Build**:
   - Click **"Save"** to apply the configuration.
   - To run the pipeline, click **"Build Now"** from the job's main page.

There should be a report of test output once the build finishes

# PetShop testing

## Setup

To run tests for excercise-2:

 - Set up a python venv with
   ```
   python3 -m venv testenv
   source testenv/bin/activate
   pip install -r requirements-2.txt
   ```
- Run the tests with logs from root using
   ```
   pytest tests/petstore/test_petstore -o log_cli=true --log-cli-level=INFO
   ```
- You can also run a specific class of tests or method using the following format seperated by ':'
   ```
   pytest tests/petstore/test_petstore.py:<test class to run>:<test method to run>
