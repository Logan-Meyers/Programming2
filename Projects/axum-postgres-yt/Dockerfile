# starting from rust:alpine
FROM rust:alpine3.20 as builder
# doing everything inside a specific directory, we don't want to have an unreadable filesystem
WORKDIR /usr/src/interface

RUN apk update --no-cache \
    && apk upgrade --no-cache \
    && apk add build-base openssl-dev pkgconfig
# copying everything from the current directory into /interface in the docker container
COPY . .

# RUN cargo install --path .
RUN cargo run
EXPOSE 8000
CMD ["interface"]