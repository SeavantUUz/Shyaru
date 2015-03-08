# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/2/28'

from traceback import format_exc as einfo

from evaluations import *
from environment import environment


def sh_eval(ast, env=None):
    if env is None:
        env = environment()
    class_ = class_mapping.get(ast.id)
    if not class_:
        class SubValue(Value):
            pass
        methods = methods_mapping[ast.id]
        for name, method in methods:
            SubValue.name = method
        class_mapping[ast.id] = SubValue
        class_= SubValue
    return ast.eval(ast, env, class_)
