# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/4/12'

from ..evaluations import Base

class While(Base):
    def __init__(self):
        super(While, self).__init__()
        self.instant_eval = False

    def set_result(self, value):
        self.result = value

    def eval(self, env):
        while_node = type(self)()
        while_node.set_result(self.result)
        return while_node

    def bool_value(self, item):
        result = item.value
        if result:
            return True
        else:
            return False

    def __str__(self):
        result = getattr(self, 'result', None)
        return '{}'.format(result)
