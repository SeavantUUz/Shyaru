# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/3/8'

__all__ = ['BASE']

class Base(object):
    def __init__(self, value=None):
        if value is not None:
            self.value = value
        self.instant_eval = True
        self.left = None
        self.right = None

    def set(self, value):
        if self.left is None:
            self.left = value
        elif self.right is None:
            self.right = value
        else:
            raise TypeError("Too many assignment")

    def eval(self, env):
        raise NotImplementedError("No implemented")
