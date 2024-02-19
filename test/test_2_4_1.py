import pytest 
from src.E_2_4_1 import *

def test_organizador():
    assert organizador([8, 3, 1, 19, 14]) == [1, 3, 8, 14, 19]