# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/2/28'

__all__ = ['sh_eval']

from .evaluations.factory import typeFactory
from .environment import Environment
from .evaluations.names import Name
from .evaluations.if_statement import If
from .evaluations.while_statement import While
from .evaluations.function import Function
from .evaluations.lparent import LParent


def sh_eval_list(ast_list, env=None, args=None):
    # 只把最后的结果返回去
    if not type(ast_list) == list:
        ast_list = [ast_list]
    final_result = None
    if env is None:
        env = Environment()
    else:
        env = env.fork()
    if args is not None:
        for key in args:
            env.set(key, args[key])
    for ast in ast_list:
        final_result = sh_eval(ast, env)
        print "{}->{}".format(ast, final_result)
    env.delete()
    return final_result


def sh_eval(ast, env):
    if ast is None:
        return None
    Node = typeFactory(ast.id)
    if not Node:
        raise SyntaxError('Unsupported Type: {}'.format(ast.id))
    if not getattr(ast, 'left', None) and not getattr(ast, 'right', None):
        node = Node(ast.value)
        if isinstance(node, Name):
            try:
                node = env.get(ast.value)
            except NameError:
                node = node
        return node
    node = Node()
    instant_eval = node.instant_eval
    if instant_eval:
        left = sh_eval(getattr(ast, 'left', None), env)
        if left is not None:
            node.set(left)
        right = sh_eval(getattr(ast, 'right', None), env)
        if right is not None:
            node.set(right)
    else:
        if isinstance(node, If):
            # only for test
            left = sh_eval(getattr(ast, 'left', None), env)
            right = getattr(ast, 'right', None)
            if node.bool_value(left.eval(env)):
                if_result = sh_eval_list(right, env)
                node.set_result(if_result)
        elif isinstance(node, While):
            left = sh_eval(getattr(ast, 'left', None), env)
            right = getattr(ast, 'right', None)
            while node.bool_value(left.eval(env)):
                while_result = sh_eval_list(right, env)
                node.set_result(while_result)
        elif isinstance(node, Function):
            func_name = getattr(ast, 'left', None)
            args_list = getattr(ast, 'right', None)
            extra = getattr(ast, 'extra', None)
            node.func_name = func_name
            node.args_list = args_list
            node.block = extra
            env.set(node.get_func_name(), node)
            print node
            node.set_result(None)
        elif isinstance(node, LParent):
            orig_func_name = getattr(ast, 'left', None)
            try:
                func_name = orig_func_name.value
                func = env.get(func_name, None)
            except Exception:
                func = None
            if not func:
                raise SyntaxError("Function {} could not be found".format(orig_func_name))
            parameters_list = getattr(ast, 'right', [])
            parameters = dict()
            for name, parameter in zip(func.get_args(), parameters_list):
                # 对name讨论的时候再看
                # value = parameter.eval(env)
                Node_ = typeFactory(parameter.id)
                node_ = Node_(parameter.value)
                parameters[name] = node_
            func_result = sh_eval_list(func.get_block(), env, parameters)
            node.set_result(func_result)
    return node.eval(env)
