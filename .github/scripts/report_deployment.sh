#!/bin/bash

OUT=$(cat $1)
DURATION=$(echo $OUT | grep "real" | grep -o "[0-9][a-z0-9\.]\+")
STATUS=$(echo $OUT | grep -oP '(?<=STATUS\: )\w+')
DATE=$(echo $OUT | grep -oP '(?<=LAST DEPLOYED\: )[^\n]+')
GIT_TOKEN=$2
REMOTE="https://$GITHUB_ACTOR:$GIT_TOKEN@github.com/$GITHUB_REPOSITORY.git"

setup_git() {
  # initializes git info
  git config --local user.email "action@github.com"
  git config --local user.name "GitHub Action"
}

push_report() {
  git add .
  git commit -m "Submitting report for deployment from $DATE"
  git push "$CHART_REMOTE" "HEAD:$GIT_BRANCH" -v -v
}

setup_git
python .github/scripts/report_deployment.py anvil '{"status": "$STATUS", "time": "$DURATION", "date": "$DATE"}'
push_report
