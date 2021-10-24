#!/bin/bash
set -e

#check number of args
if ! [[ $# -eq 1 ]];
then
  echo "VERSION ARGUMENT REQUIRED"
  exit 1
fi

VERSION="$1"

cd python_backend

echo 'run docker build urbanjungle/springer:$BUILD_ENV-$VERSION-$PROVIDER_MODULE'
docker build -t benleong0/japanese_vocab_fetcher:$VERSION .
echo 'DOCKER BUILD COMPLETE'
docker push benleong0/japanese_vocab_fetcher:$VERSION
echo 'DOCKER PUSH COMPLETE'
echo 'DOCKER BUILDING AND PUSHING FINISHED'

echo "FINISHED"
