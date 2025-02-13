set -eu
python3 11.py | sha384sum
expand -t 1 popular-names.txt | sha384sum
