# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/3/14'


def string_add(self, other):
    r_str =  ''.join([self.value, other.value])
    print self.value
    return type(self)(r_str)


def string_sub(self, other):
    raise TypeError("unsupported operand type(s) for -: 'str' and '{}'".format(type(other.value)))


def string_mul(self, other):
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


def string_div(self, other):
    raise TypeError("unsupported operand type(s) for /: 'str' and '{}'".format(type(other.value)))


def string_evaluate(self, env, value_type):
    return value_type(self.value)


def init_methods():
    r = dict()
    r['(string)'] = [('__add__', string_add),
                     ('__sub__', string_sub),
                     ('__mul__', string_mul),
                     ('__div__', string_div)]
    return r


def init_eval():
    r = dict()
    r['(string)'] = string_evaluate
    return r
