#!/usr/bin/env python3

import cgi
import html
import sqlite3
import sys
import io

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

conn = sqlite3.connect('todolist.db')
curs = conn.cursor()


print('Content-type: text/html')
print('')


def print_html(data=""):
    print('''\
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <title>Todoリスト</title>
    </head>
    <body>
    <form action="todo.py" method="post">
    タスク名<input type="text" name="name">
    <input type="hidden" name="mode" value="add">
    <input type="submit" value="追加">
    </form>
    <ul>
    {0}
    </ul>
    </body>
    </html>
    '''.format(data))


form = cgi.FieldStorage()
mode = form.getvalue('mode')

if mode == 'add':
    name = form.getvalue('name')
    name = html.escape(name)

    sql = ('INSERT INTO tasks(name) VALUES (?)')
    curs.execute(sql, (name,))
    conn.commit()

if mode== 'done':
    id=form.getvalue('id')
    id=html.escape(id)

    sql=('DELETE FROM tasks WHERE id=?')
    curs.execute(sql,(id,))
    conn.commit()

curs.execute('SELECT * FROM tasks')
rows = curs.fetchall()

data = ""

for id,name in rows:
    data +=  '''
    <li>{0}
    <form action="todo.py" method="post">
    <input type="submit" value="済んだ">
    <input type="hidden" name="id" value="{1}">
    <input type="hidden" name="mode" value="done">
    </form>
    </li>
    '''.format(name,id)

print_html(data)
