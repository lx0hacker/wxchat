#!/bin/bash
if [ ! -d "logs" ]; then
    mkdir logs
fi
echo "Start new gunicorn......"
source venv/bin/activate
gunicorn -c gunicorn.py wxchat:app