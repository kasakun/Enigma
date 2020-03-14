#!/usr/bin/python3
"""Helper to generate a rotor"""
__author__ = 'kasakun'
__verison__ = '1.0'

# Not all ascii code can be displayed
# Printable ASCII: 32 - 126. Thus there is a bias as 30
# Remap 0-94: 32-126
#       95  : \n
#       96  : \t
ASCII = [x for x in range(97)]
ASCII_BIAS = 32

import random

class Generator:
    """Gnerate a random template for rotor"""
    def __init__(self):
        pass

    def get(self):
        _list = ASCII.copy()
        _res = []

        while len(_list) > 0:
            index = random.randint(0, 127) % len(_list)
            _res.append(_list.pop(index))

        return _res

    def get_ascii(self):
        _list = [chr(x + 30) for x in ASCII]
        _res = []

        while len(_list) > 0:
            index = random.randint(0, 127) % len(_list)
            _res.append(_list.pop(index))

        return _res

class Rotor:
    """Generic Rotor"""
    def __init__(self, rotor):
        self._rotor = rotor
        self._base = 0
        self._size = len(self._rotor)

    def map_forward(self, index):
        ret = self._rotor[(index + self._base)%self._size]
        return ret

    def map_backward(self, num):
        ret = (self._rotor.index(num) + self._size - self._base)%self._size
        return ret

    def rotate(self):
        self._base = (self._base + 1)%self._size

    def reset(self):
        self._base = 0

    def get(self):
        return self._rotor

    def get_size(self):
        return self._size

    def print_rotor(self):
        print(self._rotor)

class RotorAscii(Rotor):
    """Ascii Rotor"""
    def __init__(self):
        gen = Generator()
        self._rotor = gen.get()
        self._base = 0
        self._size = len(self._rotor)

    @staticmethod
    def preprocess(num):
        """Method to convert a char to ascii array"""
        if num == ord('\n'):
            return 95
        if num == ord('\t'):
            return 96
        return num - ASCII_BIAS

    @staticmethod
    def postprocess(num):
        if num == 95:
            return ord('\n')
        if num == 96:
            return ord('\t')
        return num + ASCII_BIAS

if __name__ == '__main__':
    pass
