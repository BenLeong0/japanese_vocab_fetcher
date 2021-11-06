#!/bin/bash
set -e

#check number of args
if ! [[ $# -eq 3 ]];
then
  echo "ARGUMENTS REQUIRED: VERSION, FORVO API KEY AND WANIKANI API KEY"
  exit 1
fi

VERSION="$1"
FORVO_API_KEY="$2"
WANIKANI_API_KEY="$3"

cd python_backend

echo 'run docker build urbanjungle/springer:$BUILD_ENV-$VERSION-$PROVIDER_MODULE'
docker build -t benleong0/japanese_vocab_fetcher:$VERSION --build-arg forvo_api_key=$FORVO_API_KEY --build-arg wanikani_api_key=$WANIKANI_API_KEY .
echo 'DOCKER BUILD COMPLETE'
docker push benleong0/japanese_vocab_fetcher:$VERSION
echo 'DOCKER PUSH COMPLETE'
echo 'DOCKER BUILDING AND PUSHING FINISHED'

echo "FINISHED"
