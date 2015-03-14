# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/3/8'

__all__ = ['methods_mapping', 'class_mapping', 'eval_mapping', 'Value']


class Value(object):
    def __init__(self, value):
        self.value = value

    def set_id(self, type):
        raise NotImplementedError('NoImplemented')

    def set_error(self, error):
        self.error = error

    def __add__(self, other):
        raise NotImplementedError('NoImplemented')

    def __str__(self):
        if getattr(self, 'error', None):
            return "error: {}".format(self.error)
        return "value: {}".format(self.value)


def init_methods():
    methods_mapping = dict()
    from numbers import init_methods
    methods_mapping.update(init_methods())
    from operations import init_methods
    methods_mapping.update(init_methods())
    from strings import init_methods
    methods_mapping.update(init_methods())
    return methods_mapping


def init_eval():
    eval_mapping = dict()
    from numbers import init_eval
    eval_mapping.update(init_eval())
    from operations import init_eval
    eval_mapping.update(init_eval())
    from strings import init_eval
    eval_mapping.update(init_eval())
    return eval_mapping


methods_mapping = init_methods
eval_mapping = init_eval
class_mapping = dict
