# test_calculator.py
#from calculator import add, subtract
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from HW1.simplepython import is_prime , squaresum , fact

def test_is_prime1():
    assert is_prime(2) == True  # This should pass

def test_is_prime2():
    assert is_prime(3) == True
    
def test_is_prime3():
    assert is_prime(4) != True  # This should pass

def test_is_prime4():
    assert is_prime(6) != True

def test_fact():
    assert fact(5) == 120

def test_squaresum():
    assert squaresum(6) != 55

def test_squaresum2():
    assert squaresum(5) == 55



