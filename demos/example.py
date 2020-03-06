#!/usr/bin/python3
"""Example"""
__author__ = 'kasakun'
__verison__ = '1.0'

import random

TEXT = ("""To nanako: Meeting you was fate, """
        """and falling in love with you was out of my control."""
        """ Unfortunately, currently we do not support \\n now. QAQ""")

from termcolor import colored
from enigma.enigma import Enigma

if __name__ == "__main__":

    random.seed(142857)

    # Create a 10-rotor enigma
    enigma = Enigma(10)

    plain = TEXT
    output = colored(plain, 'yellow')
    print(f'The plain text: \n{output}')

    secret = enigma.encrypt(plain)
    output = colored(secret, 'blue')
    print(f'The ciphered text: \n{output}')
    deciphered = enigma.decrypt(secret)
    output = colored(deciphered, 'green')
    print(f'The deciphered text: \n{output}')