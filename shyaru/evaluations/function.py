# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/4/27'

from ..evaluations import Base

class Function(Base):
    def __init__(self):
        super(Function, self).__init__()
        self.instant_eval = False
        self.result = None
        self.func_name = 'default'

    def set_result(self, value):
        self.result = value

    def eval(self, env):
        func_node = type(self)()
        func_node.set_result(self.result)
        return func_node

    def get_func_name(self):
        func_name = self.func_name.value
        return func_name

    def get_args(self):
        return map(lambda arg: arg.value, self.args_list)

    def get_block(self):
        return self.block

    def __str__(self):
        func_name = getattr(self.func_name, 'value', None)
        if func_name:
            return 'func: {}'.format(self.func_name.value)
        else:
            return 'func: {}'.format('default')