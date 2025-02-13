#!/bin/bash
set -eu
python3 12.py
diff -s col1.txt <(cut -f 1 popular-names.txt)
diff -s col2.txt <(cut -f 2 popular-names.txt)
