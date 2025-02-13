set -eu
python3 14.py 3 | sha384sum
head -n 3 popular-names.txt | sha384sum
