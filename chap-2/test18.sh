set -eu

python3 18.py | sha384sum
sort -k 3 -n -r -s popular-names.txt | sha384sum
