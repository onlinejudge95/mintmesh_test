#!/bin/bash

source .env

gunicorn --workers 2 "src.app:create_app()"
