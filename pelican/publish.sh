#!/usr/bin/env bash
rsync -v -r ../build/* kecebongsoft@web321.webfaction.com:/home/kecebongsoft/webapps/blog/
rsync -v -r ../externals/* kecebongsoft@web321.webfaction.com:/home/kecebongsoft/webapps/blog/
