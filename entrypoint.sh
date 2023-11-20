#!/bin/bash

# Waiting MySQL to be raedy
until nc -z -v -w30 db 3306
do
  echo "Waiting MySQL to be ready"
  sleep 1
done
echo "MySQL is ready."

uvicorn main:app --host 0.0.0.0 --port 8080