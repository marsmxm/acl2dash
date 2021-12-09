#!/usr/local/bin/python
import os, re, sqlite3
from bs4 import BeautifulSoup

RES_PATH = 'ACL2.docset/Contents/Resources'
# conn = sqlite3.connect(RES_PATH + '/docSet.dsidx')
conn = sqlite3.connect('docSet.dsidx')
cur = conn.cursor()

try: 
    cur.execute('DROP TABLE searchIndex;')
except: 
    pass

cur.execute('CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);')
cur.execute('CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);')

docpath = RES_PATH + '/Documents'

with open(os.path.join(docpath, 'index.html')) as page:
    soup = BeautifulSoup(page, 'lxml')

    any = re.compile('.*')
    links = soup.find_all('a', {'href': any})
    for link in links:
        name = link.text.strip()
        if len(name) > 1:
            path = link.attrs['href'].strip()
            if path != 'index.html':
                cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'func', path))
                print('name: %s, path: %s' % (name, path))

conn.commit()
conn.close()