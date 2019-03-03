#!/bin/bash

set -e

python main.py
git add -A .
git commit -m "."
git push origin master
