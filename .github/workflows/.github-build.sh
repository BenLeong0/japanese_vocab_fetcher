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
docker build --build-arg rmq_host=$RMQ_HOST --build-arg mode=$SERVICE_MODE --rm -t urbanjungle/springer:$BUILD_ENV-$VERSION-$PROVIDER_MODULE .
echo 'DOCKER BUILD COMPLETE'
docker push urbanjungle/springer:$BUILD_ENV-$VERSION-$PROVIDER_MODULE
echo 'DOCKER PUSH COMPLETE'
echo 'DOCKER BUILDING AND PUSHING FINISHED'

echo "FINISHED"
