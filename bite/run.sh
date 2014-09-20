#!/bin/sh
python3.4 manage.py migrate
python3.4 manage.py runserver 80
