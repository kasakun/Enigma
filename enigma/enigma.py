#!/usr/bin/python3
"""Implementation of engima"""
__author__ = 'kasakun'
__verison__ = '1.0'

import random
from enigma.rotor import Generator, RotorAscii, ASCII

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
        self._reflector = [abs(x - len(ASCII) + 1) for x in range(len(ASCII))]

    def encrypt_char(self, plain):
        """Encrypt a single char"""
        temp = ord(plain)

        temp = RotorAscii.remove_bias(temp)

        # forward
        for i in range(len(self._group)):
            temp = self._group[i].map_forward(temp)

        # reflect
        temp = self._reflector[temp]

        # backward
        for i in range(len(self._group) - 1, -1, -1):
            temp = self._group[i].map_backward(temp)

        temp = RotorAscii.add_bias(temp)

        self.rotate()

        return chr(temp)

    def encrypt(self, plain):
        """Encrypt a string"""
        return ''.join(list(map(self.encrypt_char, [x for x in plain])))

    def decrypt(self, secret):
        """Decrypt"""
        self.reset()
        return ''.join(list(map(self.encrypt_char, [x for x in secret])))

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
        for i in range(self._size):
            self._counter[i] = 0

if __name__ == '__main__':
    pass
