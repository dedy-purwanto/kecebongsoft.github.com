#!/usr/bin/env bash
source env/bin/activate
pelican . -o ../build/ -s pelican.conf.py
