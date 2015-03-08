# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/3/8'

__all__ = ['add_evaluate', 'sub_evaluate', 'mul_evaluate', 'div_evaluate']

from traceback import format_exc as einfo


def add_evaluate(ast, env, value_type):
    from shyaru.sh_eval import *
    if not getattr(ast, 'left') and not getattr(ast, 'right'):
        return ast
    left = sh_eval(ast.left, env)
    right = sh_eval(ast.right, env)
    try:
        result = left.__add__(right)
    except Exception:
        print einfo()
        raise TypeError("can't add {} and {}".format(type(left), type(right)))
    else:
        return result


def sub_evaluate(ast, env):
    left = sh_eval(ast.left, env)
    right = sh_eval(ast.right, env)
    try:
        result = left.__sub__(left, right)
    except Exception:
        raise TypeError("can't sub {} and {}".format(type(left), type(right)))
    else:
        return result


def mul_evaluate(ast, env):
    left = ast.eval(env)
    right = ast.eval(env)
    try:
        result = left.__mul__(left, right)
    except Exception:
        raise TypeError("can't mul {} and {}".format(type(left), type(right)))
    else:
        return result


def div_evaluate(ast, env):
    left = ast.eval(ast.left, env)
    right = ast.eval(ast.right, env)
    try:
        result = left.__div__(left, right)
    except Exception:
        raise TypeError("can't div {} and {}".format(type(left), type(right)))
    else:
        return result


def init_methods():
    return dict()


def init_eval():
    r = dict()
    r['+'] = add_evaluate
    r['-'] = sub_evaluate
    r['*'] = mul_evaluate
    r['/'] = div_evaluate
    return r
