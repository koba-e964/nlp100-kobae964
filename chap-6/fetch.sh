set -eu

if sha384sum -c sha384sum.txt; then
  exit 0
fi

echo Fetching...

curl -O https://archive.ics.uci.edu/static/public/359/news+aggregator.zip
unzip -o news+aggregator.zip
rm -rf __MACOSX
sha384sum -c sha384sum.txt
