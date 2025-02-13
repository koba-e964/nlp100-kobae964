set -eu

python3 17.py | sha384sum
cut -f 1 popular-names.txt | sort | uniq | sha384sum
