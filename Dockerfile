FROM python:3-onbuild

MAINTAINER Tasdik Rahman <tasdik.rahman@wingify.com>

CMD ["make", "run"]
# WORKDIR is changed to '/usr/src/app'
# [root:user]:/usr/src/app# ls
# Dockerfile  LICENSE  Makefile  README.md  bumblebee  requirements.txt  run.py  scripts

WORKDIR "/usr/src/app"