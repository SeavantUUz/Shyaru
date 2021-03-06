# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/3/8'

__all__ = ['Add', 'Sub', 'Mul', 'Div', 'Assign']

from ..evaluations import Base
from .names import Name

class Add(Base):
    def __init__(self):
        super(Add, self).__init__()

    def eval(self, env):
        result = self.left.eval(env).__add__(self.right.eval(env))
        return result

class Sub(Base):
    def __init__(self):
        super(Sub, self).__init__()

    def eval(self, env):
        result = self.left.eval(env).__sub__(self.right.eval(env))
        return result

class Mul(Base):
    def __init__(self):
        super(Mul, self).__init__()

    def eval(self, env):
        result = self.left.eval(env).__mul__(self.right.eval(env))
        return result

class Div(Base):
    def __init__(self):
        super(Div, self).__init__()

    def eval(self, env):
        result = self.left.eval(env).__div__(self.right.eval(env))
        return result

class Assign(Base):
    def __init__(self):
        super(Assign, self).__init__()

    def eval(self, env):
        if not isinstance(self.left, Name):
            raise SyntaxError("can't assign to literal")
        return env.set(self.left.value, self.left.store(self.right.eval(env)))


class Equal(Base):
    def __init__(self):
        super(Equal, self).__init__()

    def eval(self, env):
        result = self.left.eval(env).__eq__(self.right.eval(env))
        return result
