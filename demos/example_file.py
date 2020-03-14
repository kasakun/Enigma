#!/usr/bin/python3
"""Encode/Decode a file"""
__author__ = 'kasakun'
__verison__ = '1.0'

import random
import argparse
from enigma.enigma import Enigma

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--file', default='example_3.txt',
                        help='.txt file to input.')
    args = parser.parse_args()
    if args.file == 'example_3.txt':
        # default seed for example_3.txt
        input_seed = '3'
    else:
        # Let user choose the seed
        print('Please input a seed')
        input_seed = input('seed:')

    random.seed(input_seed)

    # Create a random size enigma
    enigma = Enigma(random.randint(5, 15))

    with open(args.file, 'r') as f:
        # Assuming the text file is not large
        input_string = f.read()

        # Eliminate the last \n
        output = enigma.encrypt(input_string[:-1])

        print('Result:')
        print(output)
