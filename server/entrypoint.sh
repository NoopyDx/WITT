#!/bin/sh

gunicorn --chdir backend -w 2 --threads 2 -b 0.0.0.0:8000 server:app