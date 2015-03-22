# coding: utf-8
__all__ = ['Number']
__author__ = 'AprocySanae'
__date__ = '15/3/5'

from shyaru.evaluations import Base

class Number(Base):
    def __init__(self, value):
        if type(value) == str:
            if '.' in value:
                value = float(value)
            else:
                value = long(value)
        else:
            value = value
        super(Number, self).__init__(value)

    def __add__(self, other):
        return type(self)(self.value + other.value)

    def __sub__(self, other):
        return type(self)(self.value - other.value)

    def __mul__(self, other):
        return type(self)(self.value * other.value)

    def __div__(self, other):
        return type(self)(self.value / other.value)

    def __str__(self):
        return '%s' % self.value

    def eval(self, env):
        return type(self)(self.value)
