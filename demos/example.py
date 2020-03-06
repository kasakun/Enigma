#!/usr/bin/python3
"""Implementation of engima"""
__author__ = 'kasakun'
__verison__ = '1.0'

TEXT = (""""Just remember that the things you put into your head are there forever,he said.\n"""
        """You might want to think about that. You forget some things, dont you? Yes.\n"""
        """You forget what you want to remember and you remember what you want to forget.\n"""
        """                                                   – Cormac McCarthy, The Road""")

from enigma.enigma import Enigma

if __name__ == "__main__":
    enigma = Enigma(4)

    plain = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'


    print(f'The plain text: \n{plain}')
    ciphered = enigma.encrypt(plain)
    print('=================================================================')
    print(f'The ciphered text: \n{ciphered}')
    print('=================================================================')
    enigma.reset()
    print(f'The deciphered text: \n{enigma.encrypt(ciphered)}')