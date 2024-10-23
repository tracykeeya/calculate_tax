import pytest

from fibonacci import fibonacci

def test_fibonacci_0():
    assert fibonacci(0)==0

def test_fibonacci_1():
    assert fibonacci(1) == 1

def test_fibonacci_5():
    assert fibonacci(5) == 5

def test_fibonacci_10():
    assert fibonacci(10) == 55
