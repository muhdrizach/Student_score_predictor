#!/usr/bin/env bash
# Install Python 3.9 manually and set it as default
echo "Setting up Python 3.9 manually"
pyenv install 3.9.13 -s
pyenv global 3.9.13

pip install --upgrade pip
pip install -r requirements.txt

