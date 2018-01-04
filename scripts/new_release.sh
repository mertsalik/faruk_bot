#!/usr/bin/env bash
cd "$(dirname "$0")"
current_pwd=$PWD

version=`cat ../.git/refs/heads/master`".zip"
echo "Creating $version in dist folder..."
zip -r ${current_pwd}/../dist/${version} .. -x "*/dist/*" -x "*/venv/*" -x "*/scripts/*" -x "*/.*" -x "*/*.pyc" -x "*/__*"