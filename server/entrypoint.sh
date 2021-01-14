#!/bin/sh

gunicorn --chdir backend -w 2 --threads 2 -b 0.0.0.0:5000 server:app