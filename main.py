#coding:utf-8

import fire
from config import opt
import sqlite3
import sys
from sql.DictSql import DictSql

def add(add_vol):
    
    if all(ord(c) < 128 for c in add_vol) == True:
        dic = DictSql()
        dic.add(add_vol)
        del dic
    else:
        print('Not ENG: ', vol_str)

def add_file(vol_file):

    dic = DictSql()
    not_exist = list()

    with open(vol_file) as fp:
        for line in fp.readlines():
            if dic.add(line.rstrip('\n')) == 0:
                not_exist.append(line.rstrip('\n'))
    del dic

    with open('daily/manual.md', 'a') as fp:
        for word in not_exist:
            fp.write(word+"\n")


def search(search_vol):

    dic = DictSql()
    dic.search(search_vol)
    del dic

def list_all():

    dic = DictSql()
    dic.list_all()
    del dic

if __name__ == '__main__':
    fire.Fire()
