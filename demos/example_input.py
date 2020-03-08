#!/usr/bin/python3
"""Example"""
__author__ = 'kasakun'
__verison__ = '1.0'

import random
from enigma.enigma import Enigma

if __name__ == "__main__":
    print('Please input a seed')
    input_seed = input('seed:')

    random.seed(input_seed)

    # Create a random size enigma
    enigma = Enigma(random.randint(5, 15))

    print('Please input a 1-line string')
    input_string = input('String:')
    output = enigma.encrypt(input_string)

    print('Result:')
    print(output)