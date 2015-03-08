# coding: utf-8
__all__ = ['number_add', 'number_div', 'number_mul', 'number_sub']
__author__ = 'AprocySanae'
__date__ = '15/3/5'


def number_add(self, other):
    result = type(self)(self.value + other.value)
    return result

def number_sub(self, number):
    return self.value - number.value

def number_mul(self, number):
    return self.value * number.value

def number_div(self, number):
    return self.value / number.value

def number_evaluate(self, env):
    if '.' in self.value:
        self.value = float(self.value)
        return self
    else:
        self.value = long(self.value)
        return self

