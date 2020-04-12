#!/usr/bin/python3
"""Implementation of engima"""
__author__ = 'kasakun'
__verison__ = '1.0'

import random
from enigma.rotor import Rotor, UNICODE

class Enigma:
    """Enigma"""
    def __init__(self, num):
        # Generate a group of rotors
        self.__group = [Rotor() for i in range(num)]

        # counter for rotation
        self.__counter = [0 for i in range(num)]

        self.__size = num

        # TODO The reflector should satisfy f(x) = y, f(y) = x
        # Hardcode here as the simple list, we can random it in future
        self.__reflector = \
            [abs(x - len(UNICODE) + 1) for x in range(len(UNICODE))]

    def encrypt_char(self, plain):
        """Encrypt a single char."""
        __ret = Rotor.preprocess(plain)

        # forward
        for i in range(len(self.__group)):
            __ret = self.__group[i].map_forward(__ret)

        # reflect
        __ret = self.__reflector[__ret]

        # backward
        for i in range(len(self.__group) - 1, -1, -1):
            __ret = self.__group[i].map_backward(__ret)

        __ret = Rotor.postprocess(__ret)

        self.rotate()

        return __ret

    def encrypt(self, plain):
        """Encrypt a string."""
        return ''.join(list(map(self.encrypt_char, [x for x in plain])))

    def decrypt(self, secret):
        """Decrypt a string."""
        self.reset()
        return ''.join(list(map(self.encrypt_char, [x for x in secret])))

    def rotate(self):
        """
        Like an adder, each time we rotate 1 rotor and rotate the one next to it
        once it finished a loop.
        """
        i = 0

        while i < self.__size:
            self.__counter[i] += 1
            self.__group[i].rotate()
            if (self.__counter[i] < self.__group[i].get_size()):
                break

            self.__counter[i] = 0
            i += 1

    def reset(self):
        """Reset all rotors."""
        for rotor in self.__group:
            rotor.reset()
        for i in range(self.__size):
            self.__counter[i] = 0

if __name__ == '__main__':
    pass
