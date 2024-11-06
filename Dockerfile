FROM jenkins/jenkins:lts

USER root 

RUN apt-get update && \
    apt-get install -y docker.io && \
    rm -rf /var/lib/apt/lists/*

RUN jenkins-plugin-cli --plugins "workflow-aggregator:latest pipeline-stage-view:latest git:latest docker-workflow:latest"
