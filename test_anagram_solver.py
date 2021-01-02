# NOTE: This is meant to be ran with `pytest`, and Python 3. So to run the tests, (in a shell), so `pytest`
from anagram_solver import *

def test_solve_anagram():
    assert 'pots' in solve_anagram('tops', 'dictionary2.txt')
    assert 'pots' in solve_anagram('ToPs', 'dictionary2.txt')
    assert 'pots' in solve_anagram('to ps', 'dictionary2.txt')
    assert 'pots' in solve_anagram('!to.ps', 'dictionary2.txt')
    assert False

def test_str_sort():
    assert 'abcd' == str_sort('dcba')
    assert str_sort('pots') == str_sort('tops')
