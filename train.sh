#!/bin/bash
echo
echo "pwd"
pwd
ls 
echo "which conda"
which conda
echo "conda list"
conda list

python3 code/train.py .2 .3