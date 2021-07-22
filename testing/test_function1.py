import os
import sys

parent_dir = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, os.path.abspath(parent_dir))

from function1 import square


class TestFunction1:

    def test_small_number(self):
        assert square(3) == 9

    def test_large_number(self):
        assert square(10**6) == 10**12

    def test_negative_number(self):
        assert square(-2) == 4

    def test_zero_number(self):
        assert square(0) == 0
