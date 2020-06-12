import requests
import pandas as pd
from bs4 import BeautifulSoup

html=requests.get("https://chefgohan.gnavi.co.jp/detail/90").text
soup=BeautifulSoup(html,"html.parser")  #htmlをすべて取得

for script in soup(["script,style"]):   #scriptやstyleを含む要素を削除
    script.decompose()

text=soup.get_text()    #テキストのみを取る
lines=[line.strip() for line in text.splitlines()]  #textを改行ごとにリストに入れる

text="\n".join(line for line in lines if line)  #リストの空白要素以外をすべて文字列に戻す

print(text)
