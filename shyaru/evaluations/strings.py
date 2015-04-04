# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/3/14'

__all__ = ['String']

from ..evaluations import Base
from .boolean import Boolean

class String(Base):
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        r_str =  ''.join([self.value, other.value])
        return type(self)(r_str)

    def __sub__(self, other):
        raise TypeError("unsupported operand type(s) for -: 'str' and '{}'".format(type(other.value)))

    def __mul__(self, other):
        if type(other.value) != int:
            raise TypeError("unsupported operand type(s) for *: 'str' and '{}'".format(type(other.value)))
        r = []
        count = other.value
        string = self.value
        while count:
            count -= 1
            r.append(string)
        r_str = ''.join(r)
        return type(self)(r_str)

    def __div__(self, other):
        raise TypeError("unsupported operand type(s) for /: 'str' and '{}'".format(type(other.value)))

    def __str__(self):
        return '%s' % self.value

    def __eq__(self, other):
        if type(self) != type(other):
            return Boolean(False)
        else:
            if self.value == other.value:
                return Boolean(True)
            else:
                return Boolean(False)

    def eval(self, env):
        return type(self)(self.value)
