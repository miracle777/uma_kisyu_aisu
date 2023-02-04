#!/usr/bin/python3
# -*- coding: utf-8 -*-

#九星相性を調べるプログラム
#相性の結果を出力するプログラム
#HTMLファイルに、結果を送るプログラム
#ウェブアプリとするために、修正。
#呼び出し元は、app.py
#必要なモジュールは、appy.pyでインポートしています。

import cgi
import cgitb
import codecs
import os
import sys
import webbrowser
import csv
import re


cgitb.enable()


#馬名配列
#uma = []
uma_l = 0
#騎手名配列
#kisyu = []
kisyu_l = 0

#画数配列
#馬名：騎手の順で記録
kakusu_uma = []
kakusu_kisyu = []

#鑑定結果二次元配列
#九星:年:月：日の相性結果で記録
#18行の二次元配列の初期化
kantei_uma_kusei = []
kantei_uma_nen = []
kantei_uma_tuki = []
kantei_uma_hi = []


kantei_kisyu_kusei = []
kantei_kisyu_nen = []
kantei_kisyu_tuki = []
kantei_kisyu_hi = []



#配列宣言
kana = []
kakusu = []

kisyu_kanji = []
kisyu_kakusu = []

#エラー送信用
errer_meg = []

"""運が良い数字の組み合わせ設定"""

#0は、ダミー
#最初は、ダミーを入れておく
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


#漢字カタカナ画数データ読み込み

#カタカナ画数調べる
#Python
#CVSファイル読み込み

#csvファイルを指定
MyPath = './static/csv/kakusu-utf8.csv'

#csvファイルを読み込み
with open(MyPath) as f:

    reader = csv.reader(f)

    #csvファイルのデータをループ
    for row in reader:

        #A列を配列へ格納
        kana.append(str(row[0]))

        #B列を配列へ格納
        kakusu.append(str(row[1]))

    #デバッグ用CVS内容確認
    #print(kisyu_kanji)
    #print(kisyu_kakusu)
    # 

#漢字の画数のファイル読み込み


#CVSファイル読み込み

#csvファイルを指定
MyPath = './static/csv/kanji_DATA_BASE.csv'

#csvファイルを読み込み
with open(MyPath) as f:

    reader = csv.reader(f)

    #csvファイルのデータをループ
    for row in reader:

        #A列を配列へ格納
        kisyu_kanji.append(str(row[0]))

        #B列を配列へ格納
        kisyu_kakusu.append(str(row[1]))




#POSTデータを取得
def katakana_kantei(user_data):





    #馬名
    l = 0



    for l in range(uma_l): #馬名が入力されている間ループ
        inp2_kusei = 0
        inp_kusei = 0
        #馬の名前の文字数を取得
        length = len(uma[l])
        #カタカナとー以外かチェック

        for i in range(length):
            if uma[l][i] == "ー":
                continue
            if uma[l][i] < "ァ" or uma[l][i] > "ヶ":
                errer_meg.append("errer")
                errer_meg.append("馬名にカタカナ以外が入力されています。")
                errer_meg.append(uma[l])
                return errer_meg

        temp_uma = uma[l]

        #一文字ずつ取り出して、画数を取得
        for i in range(length):
            for j in range(len(kana)):  
                if  temp_uma[i] == kana[j]:
                    inp_kusei = inp_kusei + int(kakusu[j])
                    break
                    

        #馬名の画数の計算ができないとき
        if inp_kusei == 0:
            errer_meg.append("errer")
            errer_meg.append("馬名の画数が取得できませんでした。")
            errer_meg.append(uma[l])
            return errer_meg

        #画数保存
        kakusu_uma.append(inp_kusei)

        

        #二桁か確認
        if inp_kusei > 9:
            #二桁の場合は一桁目と二桁目を足す
            inp2_kusei = int(str(inp_kusei)[0]) + int(str(inp_kusei)[1])

        def hutaketa():
            #二桁の場合は一桁目と二桁目を足す
            inp2_kusei = int(str(inp2_kusei)[0]) + int(str(inp2_kusei)[1])
            return inp2_kusei

        #さらに二桁の場合は一桁目と二桁目を足す
        while inp2_kusei > 9:
            hutaketa(inp2_kusei)

        

        #二桁の場合の合計表示
        #print ('二桁の場合の合計＝' + str(inp2_kusei))
        #九星の位置を取得
        if inp2_kusei >0:
            kantei_uma_kusei.append(inp2_kusei)
            inp_kusei = inp2_kusei
        else:
            kantei_uma_kusei.append(inp_kusei)


      
        #print ('今日の九星との相性は')
        #今年の九星との相性を判断して表示
        #今年相性が良いのかチャック用
        kyou = 0
        for i in range(3):
            if list1[kusei_nen][i] == inp_kusei:
                #print ('一番良い相性です')
                kantei_uma_nen.append(1) #一番良い相性
                kyou = 1
                break

        if kyou == 0:    
            for i in range(4):
                if list2[kusei_nen][i] == inp_kusei:
                    #print ('良い相性です')
                    kantei_uma_nen.append(2) #良い相性
                    kyou = 1
                    break

        if kyou == 0:
            #print ('相性は悪いです')
            kantei_uma_nen.append(3) #悪い相性

        #print ('今月の九星との相性は')
        #今月の九星との相性を判断して表示
        #今月相性が良いのかチャック用
        kyou = 0


        for i in range(3):
            if list1[kusei_tuki][i] == inp_kusei:
                #print ('一番良い相性です')
                kantei_uma_tuki.append(1) #一番良い相性
                kyou = 1
                break

        if kyou == 0: 
            for i in range(4):
                if list2[kusei_tuki][i] == inp_kusei:
                    #print ('良い相性です')
                    kantei_uma_tuki.append(2) #良い相性
                    kyou = 1
                    break

        if kyou == 0:
            #print ('相性は悪いです')
            kantei_uma_tuki.append(3) #悪い相性     

        #print ('今年の九星との相性は')
        #今日の九星との相性を判断して表示
        #今日の相性が良いのかチャック用
        kyou = 0

        for i in range(3):
            if list1[kusei_hi][i] == inp_kusei:
                #print ('一番良い相性です')
                kantei_uma_hi.append(1) #一番良い相性
                kyou = 1
                break

        if kyou == 0: 
            for i in range(4):
                if list2[kusei_hi][i] == inp_kusei:
                    #print ('良い相性です')
                    kantei_uma_hi.append(2) #良い相性
                    kyou = 1
                    break

        if kyou == 0:
            #print ('相性は悪いです')
            kantei_uma_hi.append(3) #悪い相性

    #騎手の九星を判断

    for l in range(kisyu_l): #騎手名が入力されている間ループ
        inp2_kusei = 0
        inp_kusei = 0
        #騎手の名前の文字数を取得
        length = len(kisyu[l])


        #騎手名に数字が含まれているか確認
        if any(char.isdigit() for char in kisyu[l]):
            #数字が入っている場合はエラー
            errer_meg.append('errer')
            errer_meg.append('騎手名に数字が入っています')
            errer_meg.append(kisyu[l])
            return errer_meg



        temp_kisyu = kisyu[l]
        status_kata = 0 #カタカナかどうかの判定用

        #騎手の名前がカタカナかどうか判定
        for i in range(length):
            if temp_kisyu[i] in kana:
                status_kata = 1
                break

        #名前に"ー"があるかどうか判定
        if temp_kisyu.find('ー') != -1:
            status_kata = 1

        
        if status_kata == 1:
            for i in range(length):
                for j in range(len(kana)):     #カタカナの名前の場合
                    if  temp_kisyu[i] == kana[j]:
                        inp_kusei = inp_kusei + int(kakusu[j])
                        break  
        
        if status_kata == 0:
            #一文字ずつ取り出して、画数を取得
            for i in range(length):
                for j in range(len(kisyu_kanji)):   #漢字の名前の場合
                    if temp_kisyu[i] == kisyu_kanji[j]:
                        inp_kusei = inp_kusei + int(kisyu_kakusu[j])
                        break
                        


        #騎手名の画数の計算ができないとき
        if inp_kusei == 0:
            errer_meg.append("errer")
            errer_meg.append("騎手名の画数の計算ができません")
            errer_meg.append(kisyu[l])
            return errer_meg


        #inp_kusei内容表示
        kakusu_kisyu.append(inp_kusei)

        #二桁か確認
        if inp_kusei > 9:
            #二桁の場合は一桁目と二桁目を足す
            inp2_kusei = int(str(inp_kusei)[0]) + int(str(inp_kusei)[1])


        #さらに二桁の場合は一桁目と二桁目を足す
        while inp2_kusei > 9:
            hutaketa(inp2_kusei)   

            #二桁の場合の合計表示
            #print ('二桁の場合の合計＝' + str(inp2_kusei))
            

        
        #九星の位置を取得
        if inp2_kusei >0:
            kantei_kisyu_kusei.append(inp2_kusei)
            inp_kusei = inp2_kusei
        else:
            kantei_kisyu_kusei.append(inp_kusei)



        #print ('今日の九星との相性は')
        #今年の九星との相性を判断して表示
        #今年の相性が良いのかチャック用
        kyou = 0


        for i in range(3):
            if list1[kusei_nen][i] == inp_kusei:
                #print ('一番良い相性です')
                kantei_kisyu_nen.append(1) #一番良い相性
                kyou = 1
                break

        if kyou == 0:    
            for i in range(4):
                if list2[kusei_nen][i] == inp_kusei:
                    #print ('良い相性です')
                    kantei_kisyu_nen.append(2) #良い相性
                    kyou = 1
                    break

        if kyou == 0:
            #print ('相性は悪いです')
            kantei_kisyu_nen.append(3) #悪い相性

        #print ('今月の九星との相性は')
        #今月の九星との相性を判断して表示
        #今月相性が良いのかチャック用
        kyou = 0

        for i in range(3):
            if list1[kusei_tuki][i] == inp_kusei:
                #print ('一番良い相性です')
                kantei_kisyu_tuki.append(1) #一番良い相性
                kyou = 1
                break

        if kyou == 0: 
            for i in range(4):
                if list2[kusei_tuki][i] == inp_kusei:
                    #print ('良い相性です')
                    kantei_kisyu_tuki.append(2) #良い相性
                    kyou = 1
                    break

        if kyou == 0:
            #print ('相性は悪いです')
            kantei_kisyu_tuki.append(3) #悪い相性    

        #print ('今年の九星との相性は')
        #今日の九星との相性を判断して表示
        #今日相性が良いのかチャック用
        kyou = 0

        if inp2_kusei >0:
            inp_kusei = inp2_kusei

        for i in range(3):
            if list1[kusei_nen][i] == inp_kusei:
                #print ('一番良い相性です')
                kantei_kisyu_hi.append(1) #一番良い相性
                kyou = 1
                break

        if kyou == 0: 
            for i in range(4):
                if list2[kusei_nen][i] == inp_kusei:
                    #print ('良い相性です')
                    kantei_kisyu_hi.append(2) #良い相性
                    kyou = 1
                    break

        if kyou == 0:
            #print ('相性は悪いです')
            kantei_kisyu_hi.append(3) #悪い相性

        

    #l は、入力された件数
    
    #鑑定結果と知らせる通知

    #馬の九星との相性を表示の準備
    #配列変数にデータセット

    #kantei_uma_total 馬名の結果を格納する配列
    #馬名,画数,九星,今年の相性,今月の相性,今日の相性
    kantei_uma_total = []* uma_l
    #kantei_kisyu_total 騎手の結果を格納する配列
    #騎手名,画数,九星,今年の相性,今月の相性,今日の相性
    kantei_kisyu_total = []* kisyu_l

    #馬の数,0,0,年,月,日
    kantei_uma_total.append([uma_l,0,0,kusei_nen,kusei_tuki,kusei_hi])

    for i in range(uma_l) :
        kantei_uma_total.append([uma[i],kakusu_uma[i],kantei_uma_kusei[i],kantei_uma_nen[i],kantei_uma_tuki[i],kantei_uma_hi[i]])
    

    #騎手の数,0,0,年,月,日
    kantei_kisyu_total.append([kisyu_l,0,0,kusei_nen,kusei_tuki,kusei_hi])

    for i in range(kisyu_l) :
        kantei_kisyu_total.append([kisyu[i],kakusu_kisyu[i],kantei_kisyu_kusei[i],kantei_kisyu_nen[i],kantei_kisyu_tuki[i],kantei_kisyu_hi[i]])




    return kantei_uma_total,kantei_kisyu_total,"鑑定結果"


if __name__ == '__main__':
    print('馬鑑定結果')

