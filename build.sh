#!/bin/bash -eu

python highest-voted.py

cat header.html highest-voted.html tail.html > index.html
