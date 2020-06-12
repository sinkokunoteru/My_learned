import requests
import pandas as pd
from bs4 import BeautifulSoup

class html_read():
    text=[]
    lines=[]

    def require_html():
        html=requests.get("https://chefgohan.gnavi.co.jp/detail/90").text
        return html

    def create_html_list(html):
        soup=BeautifulSoup(html,"html.parser")  #htmlをすべて取得
        for script in soup(["script,style"]):   #scriptやstyleを含む要素を削除
            script.decompose()
        text.self=soup.get_text()    #テキストのみを取る
        lines.self=[line.strip() for line in text.splitlines()]  #textを改行ごとにリストに入れる
        text.self="\n".join(line for line in lines.self if line)  #リストの空白要素以外をすべて文字列に戻す

    def html_material(text):
        start=int(text.find("■材料"))
        end=int(text.find("■この料理の作り方"))
        material=text.self[start:end]
        return material

#def SQL_save():


def main():
    h=html_read()
    html=require_html()
    create_html_list(html)
    material=html_material(text)
    print(material)
    #SQLにデータを保存
    #

if __name__=="__main__":
    main()
