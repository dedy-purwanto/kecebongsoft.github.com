#!/usr/bin/env bash
GITMODULES=`grep path ../.gitmodules | sed 's/path = /\\\|/g' | sed 's/ //g' | sed 's/\t//g' | tr '\\n' '#' | sed 's/#//g' | sed 's/^\\\|//g'`
FILES='README\|pelican\|CNAME\|static'
EXCEPTIONS=$GITMODULES'\|'$FILES
ls ../ | grep -v $EXCEPTIONS | xargs -i rm -rf ../{}
source env/bin/activate
pelican . -o ../ -s pelican.conf.py
