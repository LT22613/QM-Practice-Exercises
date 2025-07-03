import pytest
import sys

from bank import value

def test_hello():
    assert value("hello") == 0

def test_h():
    assert value("ho") == 20

def test_no_h():
    assert value("bob") == 100

def test_incorrect_values():
    assert value("123bob") != 0

def test_case_insensitivity():
    assert value("Bob") == value("bob")

def test_entire_phrase():
    assert value("hello, my name is dylan") == 0