#!/bin/bash
set -e

#check number of args
if ! [[ $# -eq 1 ]];
then
  echo "VERSION ARGUMENT REQUIRED"
  exit 1
fi

if ! [[ $1 =~ ^[0-9]+.[0-9]+.[0-9]+$ ]];
then
  echo "VERSION (ARG 1) not in correct format"
  exit 1
fi

VERSION="$1"
echo "Triggering build"

echo "Checking if tag already exists on remote"
if wget -q https://registry.hub.docker.com/v1/repositories/benleong0/japanese_vocab_fetch er/tags -O -  | sed -e 's/[][]//g' -e 's/"//g' -e 's/ //g' | tr '}' '\n'  | awk -F: '{print $3}' | grep -e $VERSION$;
then
  echo "Tag for this version and build env already exists on remote"
  exit 1
fi
echo "No tag found for this version and build env on remote"

git tag -a $VERSION -m "version $VERSION"
git push origin $VERSION
