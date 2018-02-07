#!/usr/bin/env bash
GROUP='pss123er'
#GROUP='liam'
PROJECT='blog'
#REGISTRY_URL='https://hub.docker.com'
REGISTRY_URL='registry.cn-shenzhen.aliyuncs.com'
TAG='1.0.0'


docker build -t "$GROUP/${PROJECT}:${TAG}" .
#docker rm -f blog
#docker run -d --name 'blog' -p 5000:5000 liam/blog:1.0.0
#docker run -d --name 'quote-time-share-1' -v /Users/lee/Desktop/app:/var/quote/app/ -e timeShareNumber='1' --net=host xhuabu/rose-hisory:quote
docker tag ${GROUP}/${PROJECT}:${TAG} ${REGISTRY_URL}/${GROUP}/${PROJECT}:${TAG}
docker login --username=18681490507 --password=pss123er ${REGISTRY_URL}
docker push ${REGISTRY_URL}/${GROUP}/${PROJECT}:${TAG}
