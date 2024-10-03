"""This is code is to test the calculator.py"""
import sys
import os
from hw1.simplepython import is_prime, squaresum, fact  # pylint: disable=E0401
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))


def test_is_prime1():
    """Test if 2 is prime."""
    assert is_prime(2)  # This should pass

def test_is_prime2():
    """Test if 3 is prime."""
    assert is_prime(3)  # This should pass

def test_is_prime3():
    """Test if 4 is not prime."""
    assert not is_prime(4)  # This should pass

def test_is_prime4():
    """Test if 6 is not prime."""
    assert not is_prime(6)  # This should pass

def test_fact():
    """Test if factorial of 5 is 120."""
    assert fact(5) == 120  # This should pass

def test_squaresum():
    """Test if square sum of 6 is not 55."""
    assert squaresum(6) != 55  # This should pass

def test_squaresum2():
    """Test if square sum of 5 is 55."""
    assert squaresum(5) == 55  # This should pass
