FROM jenkins/jenkins:lts
RUN jenkins-plugin-cli --plugins "workflow-aggregator:latest pipeline-stage-view:latest git:latest docker-workflow:latest"
