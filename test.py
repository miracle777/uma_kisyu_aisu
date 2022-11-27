# coding: utf-8



# 今日の九星入力のプルダウン作成
kusei = [' ','一白水星','二黒土星','三碧木星','四緑木星','五黄土星','六白金星','七赤金星','八白土星','九紫火星']
print ("<select name=\'today_kusei\'>")
for i in range(10):
    print ("<option value=",i + 1,">",kusei[i + 1],"</option>")
print ("</select>")

print ("<input type=\'submit\' value=\'送信\'>")