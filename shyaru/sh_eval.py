# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/2/28'

from evaluations import Value
from environment import environment


def sh_eval(ast, env=None):
    from mapping import *
    if env is None:
        env = environment()
    class_ = class_mapping.get(ast.id)
    if not class_:
        class SubValue(Value):
            pass
        methods = methods_mapping.get(ast.id)
        if methods:
            for name, method in methods:
                setattr(SubValue, name, method)
        class_mapping[ast.id] = SubValue
        class_= SubValue
    setattr(ast, 'eval', eval_mapping[ast.id])
    return ast.eval(ast, env, class_)
