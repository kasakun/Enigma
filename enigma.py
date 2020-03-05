#!/usr/bin/python3
"""Implementation of engima"""
__author__ = 'kasakun'
__verison__ = '1.0'

import random
from rotor_generator import Generator


class Rotor:
    """Rotor"""
    def __init__(self, rotor):
        self._rotor = rotor
        self._base = 0
        self._size = len(self._rotor)

    def map_forward(self, index):
        ret = self._rotor[index + self._base]
        #print(f'encode {ret}')
        return ret

    def map_backward(self, num):
        ret = self._rotor.index(num) + self._base
        #print(f'encode {ret}')
        return ret

    def rotate(self):
        self._base = (self._base + 1)%len(self._rotor)

    def reset(self):
        self._base = 0

    def print(self):
        print(self._rotor)

class Enigma:
    """Enigma"""
    def __init__(self, num):
        gen = Generator()
        self._group = [Rotor(gen.get()) for i in range(num)]

        # TODO The reflector should satisfy f(x) = y, f(y) = x
        # Hardcode here as the simple list, we can random it in future
        self._reflector = [abs(x - 127) for x in range(128)]

    def encrypt(self, plain):
        """Encrypt a single char"""
        temp = ord(plain)

        # forward
        for i in range(len(self._group)):
            temp = self._group[i].map_forward(temp)

        # reflect
        temp = self._reflector[temp]

        # backward
        for i in range(len(self._group) - 1, -1, -1):
            temp = self._group[i].map_backward(temp)

        return chr(temp)

    def reset(self):
        """Reset the rotors"""
        for rotor in self._group:
            rotor.reset()

if __name__ == '__main__':
    random.seed(12)
    # gen = Generator()
    # r1 = Rotor(gen.get())
    # r2 = Rotor(gen.get())
    # r3 = Rotor(gen.get())
    # r1.print()

    # print(r1.map_forward(4))
    # print(r1.map_backward(r1.map_forward(4)))

    enigma = Enigma(3)

    ciphered = enigma.encrypt('o')
    print (f'Encode as {ciphered}')
    enigma.reset()
    print (f'Decode as {enigma.encrypt(ciphered)}')
