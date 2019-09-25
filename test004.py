# -*- coding: utf-8 -*-

'''
@Author : siran
@time : 2019/9/5 10:20
@File : test004.py
@Software : PyCharm
'''
from typing import List

import requests



class Hello:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return 'Hello(%s)' % self._name

class h(Hello):
    def __str__(self):
        return 'h(%s)' % self._name

def get():
    r = requests.get("https://www.baidu.com")
    print(r.request)

class test:
    def __init__(self, s= None):
        self._s = s

class D:
    def __init__(self, n=None):
        if n == None:
            self.n = []
        else:
            self.n = n

    def add(self, c):
        self.n.append(c)

class E:
    def __init__(self, neme):
        self.name = neme
        self.d = D()

    def get_hand(self):
        return self.d






if __name__ == '__main__':
    # s) = test01(2
    # s = ','.join(str(x) for x in [1 , 2, 3])
    # print(s)
    # test01(2)
    # e = E('test')
    # e.get_hand().add(1)
    # e.get_hand().add(2)
    # e.get_hand().add(3)
    # print(e.get_hand())
    l = [1,2,3, 4]
    s = l.pop(2)
    print(s)
