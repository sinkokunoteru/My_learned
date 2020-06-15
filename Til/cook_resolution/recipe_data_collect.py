import requests
import pandas as pd
from bs4 import BeautifulSoup

class html_read():
    def __init__(self):
        self.text=[]
        self.lines=[]

    def require_html(self):
        html=requests.get("https://chefgohan.gnavi.co.jp/detail/90").text
        return html

    def create_html_list(self,html):
        soup=BeautifulSoup(html,"html.parser")  #htmlをすべて取得
        for script in soup(["script,style"]):   #scriptやstyleを含む要素を削除
            script.decompose()
        self.text=soup.get_text()    #テキストのみを取る
        self.lines=[line.strip() for line in self.text.splitlines()]  #textを改行ごとにリストに入れる
        self.text="\n".join(line for line in self.lines if line)  #リストの空白要素以外をすべて文字列に戻す

    def html_material(self,text):
        start=int(text.find("■材料"))
        end=int(text.find("■この料理の作り方"))
        material=self.text[start:end]
        return material

#def SQL_save():


def main():
    h=html_read()
    html=h.require_html()
    h.create_html_list(html)
    material=h.html_material(h.text)
    print(material)
    #SQLにデータを保存
    #

if __name__=="__main__":
    main()
