# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/2/28'

from number_methods import *


handler_mapping = dict()
methods_mapping = dict()


class environment(object):
    def __init__(self, parent=None):
        self.context = dict()
        self.parent = parent

    def set(self, name, value):
        self.context[name] = value

    def get(self, name, lookup=True):
        try:
            if lookup:
                value = self.search_name(name)
            else:
                value = self.context[name]
        except Exception:
            raise NameError("name '{}' is not defined".format(name))
        else:
            return value

    def fork(self):
        new_env = type(self)(self)
        self.child = new_env
        return new_env

    def get_name_from_global(self, name):
        context = self.context
        if not self.parent is None:
            context = self.parent.context
        try:
            value = context[name]
        except Exception:
            raise NameError("name '{}' is not defined in global".format(name))
        else:
            return value

    def search_name(self, name):
        if not self.context.has_key(name):
            parent = self.parent
            if not parent:
                raise KeyError
            else:
                return parent.search_name(name)
        else:
            return self.context[name]

    def __str__(self):
        return self.context.__str__()



def int_evaluate(self, env):
    return self.value


def float_evaluate(self, env):
    return self.value


def string_evaluate(self, env):
    return self.value


def name_evaluate(self, env):
    return env.get(self.value)

def number_evaluate(self, env):
    return int(self.value)


def assign_evaluate(self, env):
    if self.left.id != '(name)':
        raise SyntaxError("can't assign to wrong type")
    right = evaluate(self.right, env)
    env[self.left.value] = right
    return right


def add_evaluate(ast, env):
    left = sh_eval(ast.left, env)
    right = sh_eval(ast.right, env)
    try:
        result = left.__add__(right)
    except Exception:
        raise TypeError("can't add {} and {}".format(type(left), type(right)))
    else:
        return result


def sub_evaluate(ast, env):
    left = sh_eval(ast.left, env)
    right = sh_eval(ast.right, env)
    try:
        result = left.__sub__(right)
    except Exception:
        raise TypeError("can't sub {} and {}".format(type(left), type(right)))
    else:
        return result


def mul_evaluate(ast, env):
    left = ast.eval(env)
    right = ast.eval(env)
    try:
        result = left.__mul__(right)
    except Exception:
        raise TypeError("can't mul {} and {}".format(type(left), type(right)))
    else:
        return result


def div_evaluate(ast, env):
    left = ast.eval(ast.left, env)
    right = ast.eval(ast.right, env)
    try:
        result = left.__div__(right)
    except Exception:
        raise TypeError("can't div {} and {}".format(type(left), type(right)))
    else:
        return result

handler_mapping['+'] = [('eval', add_evaluate)]
handler_mapping['-'] = [('eval', sub_evaluate)]
handler_mapping['*'] = [('eval', mul_evaluate)]
handler_mapping['/'] = [('eval', div_evaluate)]

handler_mapping['(number)'] = [('__add__', number_add),
                               ('__sub__', number_sub),
                               ('__mul__', number_mul),
                               ('__div__', number_div),
                               ('eval', number_evaluate)]

def sh_eval(ast, env=None):
    if env is None:
        env = environment()
    methods = handler_mapping[ast.id]
    for name, method in methods:
        setattr(ast, name, method)
    return ast.eval(ast, env)


