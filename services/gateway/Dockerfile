# Stage 1 - copu UI files from UI build
ARG UI_BUILD_VERSION=latest
FROM lazy-lab-ui:${UI_BUILD_VERSION} as ui-base

# Stage 2 - bare nginx
FROM nginx:alpine

ARG CONF_FILE=dev.conf
ENV CONF_FILE=$CONF_FILE

COPY --from=ui-base /runtime/app/dist/ /ui-bundle/
COPY configs/$CONF_FILE /etc/nginx/nginx.conf

CMD ["nginx", "-g", "daemon off;"]
