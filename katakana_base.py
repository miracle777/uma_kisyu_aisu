# -*- coding: utf-8 -*-


#カタカナ画数調べる
#Python
#CVSファイル読み込み

import csv

#配列宣言
kanji = []
kakusu = []

#csvファイルを指定
MyPath = './kakusu-utf8.csv'

#csvファイルを読み込み
with open(MyPath) as f:

    reader = csv.reader(f)

    #csvファイルのデータをループ
    for row in reader:

        #A列を配列へ格納
        kanji.append(str(row[0]))

        #B列を配列へ格納
        kakusu.append(str(row[1]))

#デバッグ用CVS内容確認
#print(kanji)
#print(kakusu)

"""運が良い数字の組み合わせ設定"""

#0は、ダミー
#二次元配列変数の最初の値は、ダミー
#一白水星の一と合わせるように、１からスタートできるようにした。
#一白水星から九紫火星までの順番でセット。
#一番運が良い相性
list1 = [
    [0,0,0],
    [6,7,0],
    [9,0,0],
    [1,0,0],
    [1,0,0],
    [9,0,0],
    [2,5,8],
    [2,5,8],
    [2,9,0],
    [3,4,0]
]

#良い相性
list2 = [
    [0,0,0,0],
    [1,3,4,0],
    [5,6,7,8],
    [3,4,9,0],
    [3,4,9,0],
    [2,6,7,8],
    [1,7,0,0],
    [1,6,7,0],
    [5,6,7,0],
    [2,5,8,0]
]

"""入力部分"""

#print ('今日の九星を入力してください')
#print ('１＝一白水星　２＝二黒土星　３＝三碧木星')
#print ('４＝四緑木星　５＝五黄土星　６＝六白金星')
#print ('７＝七赤金星　８＝八白土星　９＝九紫火星')


kusei = int(input('九星を入力してください：'))

if kusei != 1 and kusei != 2 and kusei != 3 and kusei != 4 and kusei != 5 and kusei != 6 and kusei != 7 and kusei != 8 and kusei != 9:
    print ('入力エラーです')
    exit()

inp_kusei = 0
inp2_kusei =0
#馬の名前の入力

uma = input('馬の名前を入力してください：')

#馬の名前の文字数を取得
length = len(uma)
#カタカナ以外かチェック

for i in range(length):
    if uma[i] in kanji:
        continue
    else:
        print ('カタカナ以外が入力されています')
        exit()
        

 #一文字ずつ取り出して、画数を取得
for i in range(length):
    for j in range(len(kanji)):
        if uma[i] == kanji[j]:
            inp_kusei = inp_kusei + int(kakusu[j])
            
#inp_kusei内容表示
print ('画数＝' + str(inp_kusei))

#二桁か確認
if inp_kusei > 9:
    #二桁の場合は一桁目と二桁目を足す
    inp2_kusei = int(str(inp_kusei)[0]) + int(str(inp_kusei)[1])

    #二桁の場合の合計表示
    print ('二桁の場合の合計＝' + str(inp2_kusei))

print ('この馬の九星は')
#合計から九星を判断して表示
if inp_kusei == 1 or inp2_kusei == 1:
    print ('一白水星')
elif inp_kusei == 2 or inp2_kusei == 2:
    print ('二黒土星')
elif inp_kusei == 3 or inp2_kusei == 3:
    print ('三碧木星')
elif inp_kusei == 4 or inp2_kusei == 4:
    print ('四緑木星')
elif inp_kusei == 5 or inp2_kusei == 5:
    print ('五黄土星')
elif inp_kusei == 6 or inp2_kusei == 6:
    print ('六白金星')
elif inp_kusei == 7 or inp2_kusei == 7:
    print ('七赤金星')
elif inp_kusei == 8 or inp2_kusei == 8:
    print ('八白土星')
elif inp_kusei == 9 or inp2_kusei == 9:
    print ('九紫火星')

print ('です')

print ('今日の九星との相性は')
#今日の九星との相性を判断して表示
#今日相性が良いのかチャック用
kyou = 0

if inp2_kusei >0:
    inp_kusei = inp2_kusei

for i in range(3):
    if list1[kusei][i] == inp_kusei:
        print ('一番良い相性です')
        kyou = 1

if kyou == 0:    
  for i in range(4):
      if list2[kusei][i] == inp_kusei:
          print ('良い相性です')
          kyou = 1

if kyou == 0:
    print ('相性は悪いです')
    exit()

exit()