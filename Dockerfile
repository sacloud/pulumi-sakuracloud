FROM golang:1.16
MAINTAINER Kazumichi Yamamoto <yamamoto.febc@gmail.com>

RUN  apt-get update && apt-get -y install \
        bash \
        git  \
        make \
        zip  \
        bzr  \
        jq \
      && apt-get clean \
      && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

RUN curl -fsSL https://get.pulumi.com | sh
ENV PATH $PATH:/root/.pulumi/bin
RUN go install github.com/pulumi/pulumictl/cmd/pulumictl@latest