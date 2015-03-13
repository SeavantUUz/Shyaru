# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/3/8'

__all__ = ['add_evaluate', 'sub_evaluate', 'mul_evaluate', 'div_evaluate']

import logging
from traceback import format_exc as einfo

from shyaru.sh_eval import *

def _number_evaluate(attr):
    def wrapper(ast, env, value_type):
        if not getattr(ast, 'left') and not getattr(ast, 'right'):
            return ast
        left = sh_eval(ast.left, env)
        right = sh_eval(ast.right, env)
        try:
            func = getattr(left, attr)
            result = func(right)
        except Exception:
            print einfo()
        else:
            return result
    return wrapper


def add_evaluate(ast, env, value_type):
    func = _number_evaluate('__add__')
    return func(ast, env, value_type)


def sub_evaluate(ast, env, value_type):
    func = _number_evaluate('__sub__')
    return func(ast, env, value_type)


def mul_evaluate(ast, env, value_type):
    func = _number_evaluate('__mul__')
    return func(ast, env, value_type)


def div_evaluate(ast, env, value_type):
    func = _number_evaluate('__div__')
    return func(ast, env, value_type)


def init_methods():
    return dict()


def init_eval():
    r = dict()
    r['+'] = add_evaluate
    r['-'] = sub_evaluate
    r['*'] = mul_evaluate
    r['/'] = div_evaluate
    return r
