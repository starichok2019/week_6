"""
В модуле написать тесты для встроенных функций filter, map, sorted,
а также для функций из библиотеки math: pi, sqrt, pow, hypot.
"""

import math

# filter
def test_filter():
    assert list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7 ])) == [2, 4, 6]   # все четные

def test_map():
    assert list(map(lambda x:  x + 2, [1, 2, 3, 4, 5])) == [3, 4, 5, 6, 7]            # на два больше

def test_sorted():
    assert list(sorted ([7 ,5 ,3 ,1 ,2 ])) == [1, 2, 3, 5, 7]                         # отсоротировано по возрастанию

def test_pi():
    assert pi < 4                       # число пи меньше четырех = истина

import math
def math.pow():
    assert(math.pow(2,5)) == 32     # возведение числа в степеь

def math.sqrt():
    assert(math.sqrt(2)) == 1,41421356237   # квадратный корень из числа

def math.hypot():
    assert(math.hypot(3, 4)) == 5,0         # корень квадратный из суммы квадратов

def math.cos():
    assert(math.cos(2* math.pi)) == 1.0     # тригонометрическая функция















