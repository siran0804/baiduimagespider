# -*- coding: utf-8 -*-

'''
@Author : siran
@time : 2019/9/2 20:18
@File : test002.py
@Software : PyCharm
'''
import tempfile
import time



if __name__ == '__main__':
    s = b'helloword'
    t = tempfile.NamedTemporaryFile(mode="wb+", delete=False)
    t.write(s)
    # t.seek(0)
    t.close()
    f = open(t.name)
    print(f.read())