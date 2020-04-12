#!/usr/bin/python3
"""Helper to generate a rotor"""
__author__ = 'kasakun'
__verison__ = '1.0'

import random
import sys

"""
Unicode:
Range: 0~sys.maxunicode

Unprintable unicode:
u0000-u001f
u007f-u009f
- '\n' is considered as an exception

Supported unicode:
CJK symbols and puctuation
Hirakana/Katakana
Hangul
Chinese
Halfwidth and Fullwidth Forms
Emoji+Symbol

@see unicode-table.com
"""
UNICODE = [x for x in range(0x0020, 0x007f)] +\
    [0x000a] +\
    [x for x in range(0x3000, 0xa000)] +\
    [x for x in range(0xff00, 0xfff0)] +\
    [x for x in range(0x1f600, 0x1f6fa)]
UNICODE_TO_INDEX = {x: UNICODE.index(x) for x in UNICODE}

class Rotor:
    """Rotor"""
    def __init__(self):
        self.__rotor = self.generate()
        self.__base = 0
        self.__size = len(self.__rotor)

    def generate(self):
        """Generate a list of index."""
        __list = [x for x in range(len(UNICODE))]
        __res = []

        while len(__list) > 0:
            # generate a random index and append it to the rotor
            index = random.randint(0, len(__list)) % len(__list)
            __res.append(__list.pop(index))

        return __res

    def map_forward(self, index):
        """Map forward, output = r(input)."""
        __ret = self.__rotor[(index + self.__base)%self.__size]
        return __ret

    def map_backward(self, num):
        """Map backward, output = r'(input)."""
        __ret = (self.__rotor.index(num) + self.__size - self.__base)%self.__size
        return __ret

    def rotate(self):
        """Rotate the rotor by 1."""
        self.__base = (self.__base + 1)%self.__size

    def reset(self):
        """Reset the rotor to the init status."""
        self.__base = 0

    def get(self):
        """Return the rotor list."""
        return self.__rotor

    def get_size(self):
        """Return thr rotor size."""
        return self.__size

    def print__rotor(self):
        """Print the rotor."""
        print(self.__rotor)

    @staticmethod
    def preprocess(unicode_char):
        """
        Method to convert unicode char to index.
        When a character enter the enigma, it is first preprocessed to convert
        it to a encoded number(so called index). This number is mapped to
        corresponding unicode. The reason is to put all supported unicode into a
        continuous space which is easy to simulate the rotation and mapping.
        """
        return UNICODE_TO_INDEX[ord(unicode_char)]

    @staticmethod
    def postprocess(index_val):
        """
        @see preprocess
        Method to convert index to a unicode character
        """
        return chr(UNICODE[index_val])

if __name__ == '__main__':
    pass
