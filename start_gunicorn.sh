#!/bin/bash
echo "Start new gunicorn......"
source venv/bin/activate
gunicorn -c gunicorn.py wxchat:app