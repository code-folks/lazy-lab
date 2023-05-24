FROM node:18-slim

RUN apt-get update && apt-get install -y openjdk-11-jre-headless && npm install -g firebase-tools

WORKDIR /runtime
COPY ./config ./
COPY ./functions ./functions

ENTRYPOINT [ "sh", "-c", "firebase --token=$(cat /run/secrets/firebase-token) --project=$(cat /run/secrets/firebase-project) --non-interactive $0 $@"]
