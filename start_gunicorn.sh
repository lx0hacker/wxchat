#!/bin/bash
mkdir logs
echo "Start new gunicorn......"
source venv/bin/activate
gunicorn -c gunicorn.py wxchat:app