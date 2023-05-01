FROM node:18-alpine

ARG MOCKOON_VERSION=latest

RUN yarn global add @mockoon/cli@$MOCKOON_VERSION pm2@latest


COPY coordinator.config.js coordinator.config.js 
# Do not run as root.
RUN adduser --shell /bin/sh --disabled-password --gecos "" mockoon
USER mockoon
EXPOSE 3000

ENTRYPOINT ["pm2"]
CMD ["start", "--attach", "coordinator.config.js"]

