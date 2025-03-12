set -eu

if sha384sum -c sha384sum.txt; then
  exit 0
fi

curl -O -sS https://nlp100.github.io/data/neko.txt
sha384sum -c sha384sum.txt
