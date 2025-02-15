set -eu

curl -O -sS https://nlp100.github.io/data/jawiki-country.json.gz
gunzip --keep --force jawiki-country.json.gz
sha384sum -c sha384sum.txt 
