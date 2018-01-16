#coding:utf-8

import fire
from config import opt
import sqlite3
import sys

def add(vol_str):
    
    if all(ord(c) < 128 for c in vol_str) == True:
        print('ENG: ', vol_str)
    else:
        print('Not ENG: ', vol_str)

def add_file(vol_file):

    print(vol_file)

def search(search_vol):
    '''
    if len(sys.argv) <= 1:
        sys.exit(1)
    else:
        search_vol = sys.argv[2]
    '''
    conn = sqlite3.connect('db/langdao-ec.db')
    c = conn.cursor()


    result = c.execute('SELECT EXISTS(SELECT * FROM vocabulary WHERE name = ?)', (search_vol, ))

    for i in result:
        exist_flag = i[0]
        break

    if exist_flag == 1:
        result = c.execute('SELECT * FROM vocabulary WHERE name = ?', (search_vol, ))

        for i in result:
            print('index: ',i[0])
            print('name: ',i[1])
            print('meaning: ', i[2].decode())
    else:
        print('the volcabulary is not exist!')

    conn.close()

if __name__ == '__main__':
    fire.Fire()
