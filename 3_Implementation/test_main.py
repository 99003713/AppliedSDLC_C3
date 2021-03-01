''' This is a pytest module '''
import pytest
from main import *


def test_sum_of_all_1():
    ''' This is a first test case for sum_of_all '''
    li1 = [[60, 45, 50, 30, 40, 20], [10, 20, 30, 40, 50, 60], [0, 0, 10, 10, 10, 50], [
        20, 20, 20, 20, 20, 20], [0, 0, 0, 0, 0, 0], [20, 20, 20, 20, 20, 20]]
    li2 = sum_of_all(li1)
    assert [245, 210, 80, 120, 0, 120] == li2


def test_sum_of_all_2():
    ''' This is a second test case for sum_of_all '''

    li1 = [[60, 45, 50, 30, 40, 20], [60, 20, 30, 40, 50, 60], [0, 90, 10, 10, 10, 50], [
        70, 20, 20, 20, 20, 20], [10, 10, 10, 10, 10, 10], [20, 20, 20, 20, 20, 20]]
    li2 = sum_of_all(li1)
    assert [245, 260, 170, 170, 60, 120] == li2


def test_average_of_all_1():
    ''' This is a second test case for average of all '''

    li1 = [[60, 45, 50, 30, 40, 20], [10, 20, 30, 40, 50, 60], [0, 0, 10, 10, 10, 50], [
        20, 20, 20, 20, 20, 20], [0, 0, 0, 0, 0, 0], [20, 20, 20, 20, 20, 20]]
    li2 = average_of_all(li1)
    assert [41, 35, 13, 20, 0, 20] == li2


def test_average_of_all_2():
    ''' This is a second test case for average of all '''
    li1 = [[60, 45, 50, 30, 40, 20], [60, 20, 30, 40, 50, 60], [0, 90, 10, 10, 10, 50], [
        70, 20, 20, 20, 20, 20], [10, 10, 10, 10, 10, 10], [20, 20, 20, 20, 20, 20]]
    li2 = average_of_all(li1)
    assert [41, 43, 28, 28, 10, 20] == li2
