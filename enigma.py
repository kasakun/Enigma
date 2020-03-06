#!/usr/bin/python3
"""Implementation of engima"""
__author__ = 'kasakun'
__verison__ = '1.0'

import random
from rotor import Generator
from rotor import RotorAscii

class Enigma:
    """Enigma"""
    def __init__(self, num):
        # Now we only condiser ASCII rotor
        self._group = [RotorAscii() for i in range(num)]

        # counter for rotation
        self._counter = [0 for i in range(num)]

        self._size = num

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

        self.rotate()

        return chr(temp)

    def rotate(self):
        """
        Like a adder, each time we rotate 1 rotor and rotate the one next to it
        once it finished a loop.
        """
        i = 0

        while i < self._size:
            self._counter[i] += 1
            self._group[i].rotate()
            if (self._counter[i] < self._group[i].get_size()):
                break

            self._counter[i] = 0
            i += 1


    def reset(self):
        """Reset all rotors"""
        for rotor in self._group:
            rotor.reset()

if __name__ == '__main__':
    pass
