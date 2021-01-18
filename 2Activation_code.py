#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import string

data = ''
codes = set()
i = 0
def random_code():
    data = string.ascii_letters + string.digits
    while True:
        activation_code = ''.join(random.sample(data,6))
        codes.add(activation_code)
        if len(codes) < 200:
            continue
        else:
            print('共生成200个激活码：' ) 
            print(codes)
            break

if __name__ == "__main__":
    random_code()
