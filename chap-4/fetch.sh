set -eu

curl -O -sS https://nlp100.github.io/data/neko.txt
sha384sum -c sha384sum.txt
