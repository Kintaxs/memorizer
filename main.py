#coding:utf-8

import fire
from config import opt
import sqlite3
import sys
from sql.DictSql import DictSql

def add(vol_str):
    
    if all(ord(c) < 128 for c in vol_str) == True:
        print('ENG: ', vol_str)
    else:
        print('Not ENG: ', vol_str)

def add_file(vol_file):

    print(vol_file)

def search(search_vol):

    dic = DictSql()
    dic.search(search_vol)
    del dic

if __name__ == '__main__':
    fire.Fire()
