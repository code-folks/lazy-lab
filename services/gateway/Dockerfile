# Stage 1 - build frontend app
FROM handy-ui as ui-base

WORKDIR /app/
RUN yarn build

# Stage 2 - nginx & frontend dist
FROM nginx:alpine

COPY gateway/prod.conf /etc/nginx/nginx.conf
COPY --from=ui-base /app/dist/ /dist/

CMD ["nginx", "-g", "daemon off;"]

