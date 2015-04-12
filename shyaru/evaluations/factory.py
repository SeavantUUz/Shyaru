# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/3/21'

from .numbers import Number
from .strings import String
from .names import Name
from .operations import Add, Sub, Div, Mul, Assign, Equal
from .if_statement import If
from .while_statement import While

type_mapping = {'(number)': Number, '(string)': String, '(name)': Name,
                '+': Add, '-': Sub, '*': Mul, '/': Div, '=': Assign, '==': Equal, 'if': If, 'while': While}

def typeFactory(type_):
    Class_ = type_mapping.get(type_, None)
    return Class_
