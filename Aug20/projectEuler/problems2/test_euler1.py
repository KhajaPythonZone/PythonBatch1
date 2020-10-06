from problems2 import euler1
import pytest


def test_traditional_solution():
    """
    In this test case we will test the traditional solution for project euler 1
    https://projecteuler.net/problem=1
    """
    assert euler1.traditional_solution(10) == 23


def test_list_comprehension():
    """
    In this test we assert for euler problem 1 using list comprehensions
    """
    assert euler1.list_comprehension_solution(10) == 23


def test_lambda():
    """
    In this test we assert for euler problem 1 using lambda expression
    """
    assert euler1.lambda_solution(10) == 23
