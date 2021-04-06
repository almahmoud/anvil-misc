#!/bin/bash
set -xe

DURATION=$(cat $1 | grep "real" | grep -o "[0-9][a-z0-9\.]\+")
STATUS=$(cat $1 | grep "STATUS:" | grep -oP '(?<=STATUS\: )\w+')
DATE=$(cat $1 | grep "LAST DEPLOYED:" | grep -oP '(?<=LAST DEPLOYED\: )[^\n]+')
REPORT_DIR=$2
GIT_TOKEN=$3
GIT_BRANCH=master
REMOTE="https://$GITHUB_ACTOR:$GIT_TOKEN@github.com/$GITHUB_REPOSITORY.git"

setup_git() {
  # initializes git info
  git config --local user.email "action@github.com"
  git config --local user.name "GitHub Action"
  git pull
}

push_report() {
  git add .
  git commit -m "Submitting report for deployment from $DATE"
  git push "$REMOTE" "HEAD:$GIT_BRANCH" -v -v
}

setup_git
mkdir -p "reports/$REPORT_DIR"
touch "reports/$REPORT_DIR/deployments.json"
touch "reports/$REPORT_DIR/deployments.html"
python .github/scripts/report_deployment.py $REPORT_DIR "{\"status\": \"$STATUS\", \"time\": \"$DURATION\", \"date\": \"$DATE\"}"
push_report
