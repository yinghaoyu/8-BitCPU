# coding=utf-8

import os
dirname = os.path.dirname(__file__)

result = b''

with open(os.path.join(dirname, 'screen.bin'), 'rb') as file:
    while True:
        b = file.read(1)
        g = file.read(1)
        r = file.read(1)
        if not r:
            break
        result += r + g + b

with open(os.path.join(dirname, 'result.bin'), 'wb') as file:
    file.write(result)
