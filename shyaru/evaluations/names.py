# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/3/15'

__all__ = ['Name']

from ..evaluations import Base

class Name(Base):
    def __init__(self, value):
        super(Name, self).__init__(value)

    def eval(self, env):
        return env.get(self.value)

