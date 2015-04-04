# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/4/4'

__all__ = ['Boolean']

from ..evaluations import Base

class Boolean(Base):
    def __init__(self, value):
        if value:
            boolean = True
        else:
            boolean = False
        super(Boolean, self).__init__(boolean)

    def __eq__(self, other):
        if type(other) != type(self):
            return type(self)(False)
        else:
            return type(self)(self.value and other.value)

    def eval(self, env):
        return type(self)(self.value)

    def __str__(self):
        return "{}".format(self.value)