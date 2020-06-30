まずはHTMLの入力フォームについて記述していく。
phpは論理的な処理をする言語でありフロントの部分についてはすべてHTML等のマークアップ言語で記述する。


テキストボックスの記入方法
---------------------------------
お名前を入力して下さい：<br>
<input type="text" name="simei">
---------------------------------

チェックボックス
---------------------------------
このHPを何で知りましたか？<br>
<input type="checkbox" name="check1" value="検索エンジン"  /> 検索エンジン経由で<br>
<input type="checkbox" name="check2" value="ポスター"  /> ポスターを見て<br>
<input type="checkbox" name="check3" value="その他"  /> その他<br>
value要素がphpに送信される
---------------------------------

ラジオボタン
---------------------------------
性別を選んで下さい。<br>
<input type="radio" name="gender" value="男性">男性です<br>
<input type="radio" name="gender" value="女性">女性です<br>
---------------------------------

セレクトボックス
---------------------------------
お問合せ種別を選んで下さい。<br>
<select name="type">
<option value="ご質問">質問がある</option>
<option value="ご要望">要望がある</option>
<option value="その他">その他の問合せ</option>
</select>
----------------------------------

テキストエリア
----------------------------------
内容を入力して下さい。<br>
<textarea name="contents" rows="5" cols="30"></textarea>
----------------------------------

webサイトにおける入力フォームについてはこれらの５つが主に挙げられる。
ここからはフォームに入力された内容をphpで受け取る方法を説明する。

フォームに入力された内容はPHPの"$_REQUEST"という連想配列として取得される。
連想配列とは、pythonで言うところの辞書型データのこと。
------------------------
$_REQUEST["フォーム名"]
------------------------
フォーム名とはname="xxx"で指定したもののこと。
------------------------
<form name="inquiry_form" action="complete.php" method="POST or GET">
------------------------
これによって、complete.phpにおいて、$_REQUEST["inquiry_form"]にデータが送信される。
