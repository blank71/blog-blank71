---
title: "Narou.rb on UserLAnd(Android)"
author: ""
type: ""
date: 2020-05-07
subtitle: ""
image: ""
tags: ["blog", "UserLAnd", "Android", "Narou.rb"]
categories: ["blog"]
---
AndroidでLinuxの環境が作れるUserLAndというアプリでUbuntuを使い、Narou.rbというものをインストールしようと思った。その備忘録。
<!--more-->
インストールはホームディレクトリで、パスなどなどは適宜読み替えること。

Narou.rbを導入するまでに必要な手順は公式に書いてあるのでそれに従う。 https://github.com/whiteleaf7/narou/wiki

### メモ
- Kindlegenは元から導入するつもりがないので導入していないが、そもそもARM向けのものがないので使えないらしい。
- AozoraEpub3で出力されるepubはGoogle Play Booksでは読み込めない。理由はググると出てくるけど正直分からない。Sony Readerで読むことができた。

### Java
Javaはどれがいいのか分からないからこのような感じにした。
````
$ sudo apt install openjdk-8-jre
````

### Ruby
Rubyはソースコードから入れようと思ったがつまずいたので、rbenvを用いた。Rubyをインストールするまでに色々なものをインストールしたのでどのライブラリが必要なのか正直分かっていない。当記事に書いてある手順ではライブラリが不足しているかもしてない。rbenvに関しては http://www.aise.ics.saitama-u.ac.jp/~gotoh/RubyByRbenvOnUbuntu1804.html を参考にした。おそらくこれでいける。

````
# 前準備
$ sudo apt install -y libssl-dev libreadline-dev zlib1g-dev
$ sudo apt install -y gcc g++ make 

# ソースを持って来る
$ cd
$ git clone https://github.com/sstephenson/rbenv.git .rbenv
$ git clone https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build

# .bashrcに書き込み
$ echo "# For rbenv" >> ~/.bashrc
$ echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
$ echo 'eval "$(~/.rbenv/bin/rbenv init -)"' >> ~/.bashrc
$ source ~/.bashrc
$ exit

# rbenvでRubyのインストール。時間がかかる。
$ rbenv install -l
$ rbenv install 2.7.1
$ rbenv rehash
$ rbenv global 2.7.1
$ ruby -v

# gemのアップデート
$ gem update --system
$ gem --version
````

### AozoraEpub3
````
$ wget https://download1.getuploader.com/g/5eb38f4d-1d64-45c8-8e58-095ea010e467/AozoraEpub3/67/AozoraEpub3-1.1.0b46.zip
## 展開する。展開先のパスを覚えておく。
$ sudo apt install unzip
$ unzip -d Aozora3 AozoraEpub3-1.1.0b46.zip
````

### Narou.rb
````
$ gem install narou
## narouのためのディレクトリを作る。名前はお好みで。
$ mkdir narou&&cd narou
## narou init 後にAozoraepub3のあるパスを聞かれる。私は $HOME/narou/Aozora3 とした。
$ narou init
> $HOME/narou/Aozora3
````

あとはNarou.rbのドキュメントを参照して使えば良い。Ubuntuの日本語化をしていないと出力時にエラーになるので日本語化しておく必要がある。
UserLAndにあるデータをAndroidのファイルマネージャーで閲覧することができないので見えるところに転送する必要がある。
````
$ cp $HOME/narou /storage/internal
````

### 感想
AndroidアプリのKindleとGoogle Play Booksはキーボードの移動に対応しており、Sony Readerは対応していない。これは少し不便。ちなみにGoogle Play Booksはページめくりが縦書きの場合は矢印キーが左右逆で対応している。些細な不便だけどこれはすぐ慣れる。

Narou.rbを導入した目的は「なろう」以外のサイトのデータを保存しつつ、それをGoogle Play Booksで閲覧することだった。だが、実際のところ、Google Play Booksにアップロードすることはできなかった。Google Play Booksの利点はまず動作が軽快であること。そして端末のepubファイルを読み込ませると自動で鯖にアップロードしてくれるので別の端末でもすぐに鯖からダウンロードして読み始めることができるという点だ。

Google Play Booksでも読み込めるようにepubを出力するように手を加えている記事があったがいまいち分からないのでどうにかしたい。

