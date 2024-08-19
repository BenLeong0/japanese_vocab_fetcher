# load env file
set -a
source .env
set +a

# login
aws ecr get-login-password --region eu-west-2 --profile personal | docker login --username AWS --password-stdin 078653112331.dkr.ecr.eu-west-2.amazonaws.com

# build
docker build\
    -f Dockerfile.lambda\
    -t japanese-vocab-fetcher\
    --build-arg forvo_api_key=$FORVO_API_KEY\
    --build-arg wanikani_api_key=$WANIKANI_API_KEY\
    .

# tag
docker tag japanese-vocab-fetcher:latest 078653112331.dkr.ecr.eu-west-2.amazonaws.com/japanese-vocab-fetcher:latest

# push
docker push 078653112331.dkr.ecr.eu-west-2.amazonaws.com/japanese-vocab-fetcher:latest
