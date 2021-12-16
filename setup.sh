#!/bin/bash -e

printf "\nClear previous virtual environment, builds, and caches\n"
rm -rf .pyaoc pyaoc/pyaoc.egg-info

# Setup virtual environment, see https://docs.python.org/3/library/venv.html
printf "\nSetup Python3.8 virtual environment and activate it\n"
python3.8 -m venv .pyaoc
source .pyaoc/bin/activate

printf "\nUpgrade pip and setuptools\n"
pip install --upgrade pip setuptools

printf "\nInstall required dependencies\n"
pip install -r requirements.txt
pip install -r requirements.local