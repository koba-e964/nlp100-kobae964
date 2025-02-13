#!/bin/bash
set -eu
python3 13.py
diff -s merged.txt <(paste col1.txt col2.txt)
