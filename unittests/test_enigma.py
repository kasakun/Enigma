# !/bin/Python3

import random
from ..enigma import Enigma
import pytest

class TestEnigmaAscii:
    def test_enigma_ascii_single_char(self):
        """Encode/decode verification"""
        random.seed(12)

        enigma = Enigma(3)

        for i in range(128):
            enigma.reset()
            plain = chr(i)

            ciphered = enigma.encrypt(plain)
            enigma.reset()
            deciphered = enigma.encrypt(ciphered)

            assert plain == deciphered
