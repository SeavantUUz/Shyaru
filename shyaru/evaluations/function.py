# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/4/27'

from ..evaluations import Base

class Function(Base):
    def __init__(self):
        super(self, Function).__init__()
        self.instant_eval = False
        self.result = None

    def set_result(self, value):
        self.result = value

    def eval(self, env):
        func_node = type(self)()
        func_node.set_result(self.result)
        return func_node

    def get_func_name(self):
        func_name = self.func_name.value
        return func_name

    def __str__(self):
        result = getattr(self, 'result', None)
        return '{}'.format(result)