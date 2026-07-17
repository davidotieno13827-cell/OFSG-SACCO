#!/usr/bin/env bash
set -e
pip install -r requirements.txt
python ofsg_platform/manage.py collectstatic --noinput
