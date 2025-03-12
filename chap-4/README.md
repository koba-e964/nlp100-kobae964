# MeCab のインストール (Mac)


```
# MeCab 本体
cd mecab-0.996/
./configure --enable-utf8-only --with-charset=utf8
make
sudo make install

# 辞書
cd ../mecab-ipadic-2.7.0-20070610
./configure --with-charset=utf8
make
make install
```
