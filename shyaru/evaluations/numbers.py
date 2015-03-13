# coding: utf-8
__all__ = ['number_add', 'number_div', 'number_mul', 'number_sub']
__author__ = 'AprocySanae'
__date__ = '15/3/5'


def number_add(self, other):
    result = type(self)(self.value + other.value)
    return result

def number_sub(self, other):
    result = type(self)(self.value - other.value)
    return result

def number_mul(self, other):
    result = type(self)(self.value * other.value)
    return result

def number_div(self, other):
    result = type(self)(self.value / other.value)
    return result

def number_evaluate(self, env, value_type):
    if '.' in self.value:
        self.value = float(self.value)
        return value_type(self.value)
    else:
        self.value = long(self.value)
        return value_type(self.value)


def init_methods():
    r = dict()
    r['(number)'] = [('__add__', number_add),
                               ('__sub__', number_sub),
                               ('__mul__', number_mul),
                               ('__div__', number_div)]
    return r


def init_eval():
    r = dict()
    r['(number)'] = number_evaluate
    return r