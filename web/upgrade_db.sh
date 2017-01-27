#!/bin/bash
set -xe

export FLASK_APP=/usr/src/app/app.py
cd /usr/src/app/bitsbox
flask db upgrade

