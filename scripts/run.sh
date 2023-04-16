#!/bin/bash

# Stop the running Python script
killall python

# Pull the latest changes from GitHub
git pull

# Install the updated requirements
pip install -r requirements.txt

# Start the Python script again
python script.py