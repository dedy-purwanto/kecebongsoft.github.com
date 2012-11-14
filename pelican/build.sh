#!/usr/bin/env bash
ls ../ | grep -v README | grep -v pelican | grep -v CNAME | grep -v static | xargs -i rm -rf ../{}
pelican . -o ../ -s pelican.conf.py
