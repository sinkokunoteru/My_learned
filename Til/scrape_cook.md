スクレイピング簡単に

html=requests.get("https://chefgohan.gnavi.co.jp/detail/90").text
HTTPで言うところのGETメソッドである。

soup=BeautifulSoup(html,"html.parser")
htmlをすべて変数に格納

text=soup.get_text()
テキストのみを取得

text[start:end]
pythonのスライス機能

明日は取得したデータをデータベースに格納するコードを作成する。
現在はまだエラーが発生しているため、まずはエラーの解消から行う。
