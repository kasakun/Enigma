# !/bin/Python3

import random
from enigma.rotor import RotorAscii, Generator
import pytest

class TestRotorAscii:
    def test_rotor_ascii_validity(self):
        """
        A ascii rotor must cover all 128 values
        """
        rotor = RotorAscii()

        for i in range(128):
            assert i in rotor.get()

    def test_rotor_ascii_size(self):
        rotor = RotorAscii()

        # Hardcode 128 as the number of ascii
        assert rotor.get_size() == 128
        assert rotor.get_size() == len(rotor.get())

    def test_rotor_ascii_forward_backward(self):
        rotor = RotorAscii()

        for plain in range(128):
            ciphered = rotor.map_forward(plain)

            assert plain == rotor.map_backward(ciphered)

    def test_rotor_ascii_rotate_map(self):
        rotor = RotorAscii()

        for _ in range(random.randint(1, 142857)):
            rotor.rotate()

        for plain in range(128):
            ciphered = rotor.map_forward(plain)
            assert plain == rotor.map_backward(ciphered)

    def test_rotor_rotate(self):
        """The encrypted char should be the same after 1 loop"""
        rotor = RotorAscii()
        plain = random.randint(0, rotor.get_size() - 1)

        c1 = rotor.map_forward(plain)
        for _ in range(rotor.get_size()):
            rotor.rotate()
        c2 = rotor.map_forward(plain)

        assert c1 == c2
