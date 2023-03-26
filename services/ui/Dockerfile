# Stage 1 - build frontend app
ARG PROJECT_DIR=handy-scan
ARG RUNTIME_DIR=/runtime/app
ARG NODE_VERSION=18

FROM node:${NODE_VERSION}-alpine as build-deps


RUN mkdir --parents $RUNTIME_DIR
COPY $PROJECT_DIR/package.json $PROJECT_DIR/yarn.lock $RUNTIME_DIR/

WORKDIR $RUNTIME_DIR/
RUN yarn install --pure-lockfile

COPY $PROJECT_DIR $RUNTIME_DIR
# COPY .env $RUNTIME_DIR/.env

EXPOSE 8080

CMD ["yarn", "serve"]

