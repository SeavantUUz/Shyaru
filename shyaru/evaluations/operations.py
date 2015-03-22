# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/3/8'

__all__ = ['Add']

from shyaru.evaluations import Base

class Add(Base):
    def __init__(self):
        super(Add, self).__init__()

    def eval(self, env):
        result = self.left.__add__(self.right)
        return result

class SUB(Base):
    def __init__(self):
        super(SUB, self).__init__()

    def eval(self, env):
        result = self.left.__sub__(self.right)
        return result

class MUL(Base):
    def __init__(self):
        super(MUL, self).__init__()

    def eval(self, env):
        result = self.left.__mul__(self.right)
        return result

class DIV(Base):
    def __init__(self):
        super(DIV, self).__init__()

    def eval(self, env):
        result = self.left.__div__(self.right)
        return result
