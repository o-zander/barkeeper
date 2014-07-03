#!/usr/bin/env bash

. env/bin/activate
django-admin.py makemessages -l de -i "env" --no-wrap --no-location
deactivate
