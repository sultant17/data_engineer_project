#!/usr/bin/env bash
/usr/local/bin/python -m pip install --upgrade pip
airflow db init
airflow users create -r Admin -u admin -e admin@example.com -f admin -l user -p admin
airflow scheduler




