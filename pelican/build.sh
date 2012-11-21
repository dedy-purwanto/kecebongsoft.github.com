#!/usr/bin/env bash
rm -rf ../build/
source env/bin/activate
pelican . -o ../build/ -s pelican.conf.py
