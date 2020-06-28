#!/bin/bash
set -e

pushd code/driver

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest
popd
