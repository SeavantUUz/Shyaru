# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/3/15'

__all__ = ['Name']

from ..evaluations import Base

class Name(Base):
    def __init__(self, value):
        super(Name, self).__init__(value)
        self.real_value = None

    def eval(self, env):
        if not self.real_value:
            self.real_value = env.get(self.value)
        return self.real_value

    def store(self, value):
        self.real_value = value
        return self

    def __str__(self):
        return '%s' % self.real_value

