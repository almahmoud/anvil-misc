#!/bin/bash
set -xe

GIT_TOKEN=$1
MESSAGE=$2
GIT_BRANCH=master
REMOTE="https://$GITHUB_ACTOR:$GIT_TOKEN@github.com/$GITHUB_REPOSITORY.git"

setup_git() {
  # initializes git info
  git config --local user.email "action@github.com"
  git config --local user.name "GitHub Action"
  git pull
}

push_report() {
  git stash
  git pull origin master
  git stash pop
  git add .
  git commit -m "$MESSAGE"
  git push "$REMOTE" "HEAD:$GIT_BRANCH" -v -v
}

setup_git
push_report
