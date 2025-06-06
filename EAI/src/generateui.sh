#!/bin/sh

filename="$1"
DIR=$(dirname $0)

if [ -z "$1" ]
then
  echo "Please input filename, ex: main"
  exit
fi

pyside2-uic gui/${filename}.ui > ui/${filename}.py
