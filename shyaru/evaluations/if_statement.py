# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/4/4'

from ..evaluations import Base

class If(Base):
    def __init__(self):
        super(If, self).__init__()
        self.instant_eval = False

    def set_result(self, value):
        self.result = value

    def eval(self, env):
        if_node = type(self)()
        if_node.set_result(self.result)
        return if_node

    def bool_value(self, item):
        result = item.value
        if result:
            return True
        else:
            return False

    def __str__(self):
        result = getattr(self, 'result', None)
        return '{}'.format(result)

