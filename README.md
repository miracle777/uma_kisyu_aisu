# uma_kisyu_aisyo
このアプリは、馬の名前と騎手の名前を入力して、調べたい年月日の九星との相性を調べます。

漢字の画数の計算は、下記のURLの作者が作られたファイルを活用しています。
https://qiita.com/kuroge/items/cc6c8167d7b9f06a1aef#comment-fa64c9c4930de0b6d7c6

馬の名前は、カタカナとーを受け付けます。
騎手の名前は、漢字と・とカタカナを受け付けます。

一応計算できない文字が入力されたときは、エラー画面が表示されます。

相性は、三段階です。
背景色で表示されます。

赤色　一番相性が良いです。
橙色　2番目に相性が良いです、
白色　相性が良くないです、

このアプリの利用で何か存在が発生しても、責任を追うことはできません。
相性の判断は、あくまで参考程度にしてください。
画数の組み合わせをすべて確認していないので、計算間違いがあるかもしれません。

##　使用した言語
PythonとFlaskを使って、作成しました。
仮想環境を作って、作りました。

## 開発環境
VSCODEとUbuntu22.04で、開発しました。

このアプリは、馬の名前と騎手の名前を入力して、調べたい年月日の九星との相性を調べます。

漢字の画数の計算は、下記のURLの作者が作られたファイルを活用しています。
https://qiita.com/kuroge/items/cc6c8167d7b9f06a1aef#comment-fa64c9c4930de0b6d7c6

馬の名前は、カタカナとーを受け付けます。
騎手の名前は、漢字と・とカタカナを受け付けます。

一応計算できない文字が入力されたときは、エラー画面が表示されます。

相性は、三段階です。
背景色で表示されます。

赤色　一番相性が良いです。
橙色　2番目に相性が良いです、
白色　相性が良くないです、

このアプリの利用で何か存在が発生しても、責任を追うことはできません。
相性の判断は、あくまで参考程度にしてください。
画数の組み合わせをすべて確認していないので、計算間違いがあるかもしれません。

##　使用した言語
PythonとFlaskを使って、作成しました。
仮想環境を作って、作りました。

## 開発環境
VSCODEとUbuntu22.04で、開発しました。

## ページ構成
#### トップページ
年、月、日の九星を選択。
騎手（選手名）、馬名の入力ページの選択

### 騎手（選手名）入力ページ

騎手（選手名）を入力。

### 馬名入力ページ
馬の名前を入力。

### 選手名鑑定結果ページ
選手の画数の診断と馬の名前入力ページへのリンク

### 馬名鑑定結果ページ
馬の画数の診断とトップページに戻るリンク
