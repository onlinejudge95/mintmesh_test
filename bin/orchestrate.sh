#!/bin/bash

source .env

gunicorn --reload --access-logfile "-" --log-level debug --workers 2 "src.app:create_app()"
