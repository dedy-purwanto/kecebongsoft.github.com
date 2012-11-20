#!/usr/bin/env bash
rsync -r ../build/* kecebongsoft@web321.webfaction.com:/home/kecebongsoft/webapps/blog/
rsync -r ../externals/* kecebongsoft@web321.webfaction.com:/home/kecebongsoft/webapps/blog/
