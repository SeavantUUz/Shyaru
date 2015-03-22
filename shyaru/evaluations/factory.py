# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/3/21'

from numbers import Number
from strings import String
from operations import Add, SUB, DIV, MUL

type_mapping = {'(number)': Number, '(string)': String, '+': Add, '-': SUB, '*': MUL, '/': DIV}

def typeFactory(type_):
    Class_ = type_mapping.get(type_, None)
    return Class_
