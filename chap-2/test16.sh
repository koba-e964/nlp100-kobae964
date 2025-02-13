set -eu

python3 16.py 4
split -l 695 -d -a 1 popular-names.txt prefix-

for i in {0..3}; do
    diff -s 16-${i}.txt prefix-${i}
done
