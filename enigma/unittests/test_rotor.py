# !/bin/Python3

import sys
import random
from enigma.rotor import Rotor, UNICODE
import pytest

class TestRotor:
    def test_rotor_validity(self):
        """A rotor must cover all unicode values."""
        rotor = Rotor()

        for i in range(len(UNICODE)):
            assert i in rotor.get()

    def test_rotor_size(self):
        """Check rotor size."""
        rotor = Rotor()

        assert rotor.get_size() == len(UNICODE)
        assert rotor.get_size() == len(rotor.get())

    def test_rotor_forward_backward(self):
        """Verify output = r(input) => input = r'(output)"""
        rotor = Rotor()

        for plain in range(len(UNICODE)):
            ciphered = rotor.map_forward(plain)

            assert plain == rotor.map_backward(ciphered)

    def test_rotor_rotate_map(self):
        """Check if rotate break the map_backward/forward."""
        rotor = Rotor()

        for _ in range(random.randint(100000, 142857)):
            rotor.rotate()

        for plain in range(len(UNICODE)):
            ciphered = rotor.map_forward(plain)
            assert plain == rotor.map_backward(ciphered)

    def test_rotor_rotate(self):
        """The encrypted char should be the same after 1 loop"""
        rotor = Rotor()
        plain = random.randint(0, rotor.get_size() - 1)

        c1 = rotor.map_forward(plain)
        for _ in range(rotor.get_size()):
            rotor.rotate()
        c2 = rotor.map_forward(plain)

        assert c1 == c2
