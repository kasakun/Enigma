# !/bin/Python3

import random
import os
from enigma.enigma import Enigma
import pytest

class TestEnigmaAscii:
    def test_enigma_ascii_single_char(self):
        """Encode/decode verification"""
        random.seed(12)

        enigma = Enigma(3)

        for i in range(32, 127):
            enigma.reset()
            plain = chr(i)

            ciphered = enigma.encrypt_char(plain)
            enigma.reset()
            deciphered = enigma.encrypt_char(ciphered)

            assert plain == deciphered

    def test_enigma_ascii_string_1(self):
        """Encode/decode verification"""
        random.seed(142857)
        enigma = Enigma(12)

        plain = 'I love nanako.'

        ciphered = enigma.encrypt(plain)

        enigma.reset()

        deciphered = enigma.encrypt(ciphered)

        assert deciphered == plain

    def test_enigma_ascii_string_2(self):
        """Encode/decode verification"""
        random.seed(142857)
        enigma = Enigma(200)

        plain = 'I love nanako.\nThe first person I would like to see everyday is you. kasakun'

        ciphered = enigma.encrypt(plain)

        enigma.reset()

        deciphered = enigma.encrypt(ciphered)

        assert deciphered == plain

    def test_large_file_ascii(self):
        """Encode/decode verification"""
        random.seed(142857)
        enigma = Enigma(15)

        curr_path = os.path.dirname(__file__)
        with open(f'{curr_path}/test_large_file_ascii.txt', 'r') as f:
            plain = f.read();

            ciphered = enigma.encrypt(plain)

            enigma.reset()

            deciphered = enigma.encrypt(ciphered)

            assert deciphered == plain
