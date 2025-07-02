set -eu

if false &&sha384sum -c sha384sum.txt; then
  exit 0
fi

curl -sSO http://download.tensorflow.org/data/questions-words.txt
curl -sSO https://www.gabrilovich.com/resources/data/wordsim353/wordsim353.zip
unzip -o wordsim353.zip
sha384sum -c sha384sum.txt
