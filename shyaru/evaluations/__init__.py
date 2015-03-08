# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/3/8'

__all__ = ['methods_mapping', 'class_mapping', 'Value']

methods_mapping = dict()
class_mapping = dict()

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
        if getattr(self, 'error'):
            return "error: {}".format(self.error)
        return "value: {}".format()