#!/bin/bash

# Let the requirements install
pip install  -r requirements.txt

#Start app
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload