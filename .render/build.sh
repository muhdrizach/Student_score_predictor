#!/usr/bin/env bash

echo "⚙️  Forcing Python 3.9.13 via pyenv..."
pyenv install 3.9.13 -s
pyenv global 3.9.13

python --version
pip install --upgrade pip
pip install -r requirements.txt
