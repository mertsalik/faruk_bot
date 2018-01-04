#!/usr/bin/env bash
cd "$(dirname "$0")"
current_pwd=$PWD
project_dir=${current_pwd}/..
venv_bin=${project_dir}/venv/bin
${venv_bin}/python3 ${project_dir}/main.py < ${project_dir}/tests/input_test.txt