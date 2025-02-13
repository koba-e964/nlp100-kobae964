set -eu

python3 19.py | sha384sum
cut -f 1 popular-names.txt | sort | uniq -c | sort -k 1 -n -r -k 2 -s | sha384sum
