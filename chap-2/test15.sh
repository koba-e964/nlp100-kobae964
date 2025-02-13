set -eu
python3 15.py 3 | sha384sum
tail -n 3 popular-names.txt | sha384sum
