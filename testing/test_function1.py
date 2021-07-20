import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from function1 import *


class TestFunction1:

  def test_small_number(self):
    assert square(3) == 9

  def test_large_number(self):
    assert square(10**6) == 10**12

  def test_negative_number(self):
    assert square(-2) == 4

  def test_zero_number(self):
    assert square(0) == 0
