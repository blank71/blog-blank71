---
title: "AndroidのUserLAndでHugoを使う"
author: ""
type: ""
date: 2020-04-10
subtitle: ""
image: ""
tags: ["hugo", "blog", "UserLAnd", "Android"]
categories: ["blog"]
---
AndroidのLinuxエミュレータの[UserLAnd](https://play.google.com/store/apps/details?id=tech.ula)
でHugoを使って静的サイトを生成するまでのお話。
<!--more-->
### はじめに
PCではHugoの環境構築ができていたけど、わざわざPCを開くまでもなくスマホだけで完結したら楽だなと思い、golangやHugoをUserLAndのUbuntu上で環境構築をしようとしていた。けど自分の無知のせいで躓くことがあった。このページはその備忘録。

### Golang
躓き、それは選択したアーキテクチャが違うということだ。PCでの私の環境はWSL on Ubuntuで、x86-64向けのものをインストールしていた。UserLAndでも同じだと思っていたのが失敗だった。


````
$ uname -a
Linux localhost 4.4.210-perf+ #1 SMP PREEMPT Wed Jan 15 11:28:15 PST 2020 aarch64 aarch64 aarch64 GNU/Linux
````

つまり、`x86-64`ではなく`aarch64`。`aarch64`は`ARMv8` 以降のものが該当する。AndroidスマートフォンのほとんどはARMだったね……。

https://golang.org/dl/ で`Arch:ARMv8`のものを選択。ファイルは`goX.XX.X.linux-arm64.tar.gz`となる。インストールはホームディレクトリにしてしまった。

````
$ wget https://dl.google.com/go/go1.14.2.linux-arm64.tar.gz
$ tar -xzf go1.14.2.linux-arm64.tar.gz
$ echo 'export PATH=$PATH:$HOME/go/bin' >> .bashrc
$ source .bashrc
$ go version
go version go1.14.2 linux/arm64
````

### Hugo
悲しいことにこちらには`extended`な`ARM64`のものが配布されていなかった。https://gohugo.io/getting-started/installing/ の`Fetch from GitHub`を参考にする。`gcc`と`g++`が必要だったので予め`sudo apt install gcc g++`としておく。

````
$ mkdir $HOME/src
$ cd $HOME/src
$ git clone https://github.com/gohugoio/hugo.git
$ cd hugo
$ go install --tags extended
$ hugo version
Hugo Static Site Generator v0.69.0-DEV/extended linux/arm64 BuildDate: unknown
$which hugo
$HOME/go/bin/hugo
````

これで完了。`/src`以下はもう必要がないので消しておいた。

### 蛇足
UserLAndではデフォルトでは日本語を入力するのに向いていないから、記事本文を書くためのMarkdownエディタのアプリと、タイトルと日にちを打ち込むだけで雛形を作って、Hugoで生成してGitHubにPushしてくれる[Pythonコード](https://github.com/blank71/blog-blank71/blob/master/hugo-new.py)を書いてみた。Pythonのコードを実行し、タイトルと日にちとMarkdownエディタで書いたものをコピペすればできあがり。まだまだ改善の余地あり。

HugoとGitHub Pagesでサイトを立ち上げたものの、テーマから引っ張ってきたままで何も手を加えていないんだけど知識もないし面倒……。ちまちまやれたらいいな。
