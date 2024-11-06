FROM jenkins/jenkins:lts

USER root
RUN apt-get update && \
    apt-get install -y python3 python3-venv docker.io curl gnupg unzip && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y wget

RUN wget -q  https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    wget -q "https://storage.googleapis.com/chrome-for-testing-public/130.0.6723.93/linux64/chromedriver-linux64.zip" -O /tmp/chromedriver.zip && \
    mkdir -p /tmp/chromedriver && \
    unzip /tmp/chromedriver.zip -d /tmp/chromedriver && \
    mv /tmp/chromedriver/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf /tmp/chromedriver /tmp/chromedriver.zip

RUN jenkins-plugin-cli --plugins "workflow-aggregator:latest pipeline-stage-view:latest git:latest docker-workflow:latest"
