set -eu

curl -O -sS https://nlp100.github.io/data/ai.ja.zip
unzip -o ai.ja.zip
sha384sum -c sha384sum.txt
