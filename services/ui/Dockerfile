# Stage 1 - build frontend app
ARG NODE_VERSION=18.16

FROM node:${NODE_VERSION}-bullseye as dependencies

ARG APP_RUNTIME=/runtime/app
ARG PROJECT_DIR=lazy-lab

ENV APP_ROOT=$APP_RUNTIME

RUN useradd -U runtime_user && mkdir --parents $APP_ROOT && chown -R runtime_user:runtime_user $APP_ROOT
COPY $PROJECT_DIR/package.json $PROJECT_DIR/yarn.lock $RUNTIME_DIR/

WORKDIR $APP_ROOT
RUN yarn install --non-interactive --pure-lockfile

FROM dependencies as base

COPY --chown=runtime_user:runtime_user $PROJECT_DIR $APP_ROOT

CMD ["yarn", "serve"]
