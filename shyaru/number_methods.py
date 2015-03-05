# coding: utf-8
__all__ = ['number_add', 'number_div', 'number_mul', 'number_sub']
__author__ = 'AprocySanae'
__date__ = '15/3/5'


def number_add(self, number):
    print self
    print number
    return self.value + number.value

def number_sub(self, number):
    return self.value - number.value

def number_mul(self, number):
    return self.value * number.value

def number_div(self, number):
    return self.value / number.value