#!/usr/bin/env bash
git pull
kill $(ps aux | grep 'daily-reading' | awk '{print $2}')
nohup gunicorn --certfile cert.pem --keyfile key.pem -k gevent -b 0.0.0.0:3030 --worker-connections 10 wsgi:app &
