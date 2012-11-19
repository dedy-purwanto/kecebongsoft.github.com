#!/usr/bin/env bash
source ~/myaws_vars
source env/bin/activate
BUCKET='kecebongsoft'
boto-rsync -g public-read ../build/ s3://kecebongsoft/blog/


