# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/2/28'

__all__ = ['sh_eval']

from .evaluations.factory import typeFactory
from .environment import Environment
from .evaluations.names import Name
from .evaluations.if_statement import If
from .evaluations.while_statement import While


def sh_eval_list(ast_list, env=None):
    # 只把最后的结果返回去
    if not type(ast_list) == list:
        ast_list = [ast_list]
    final_result = None
    if env is None:
        env = Environment()
    else:
        env = env.fork()
    for ast in ast_list:
        final_result = sh_eval(ast, env)
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
        left = sh_eval(getattr(ast, 'left', None), env)
        right = getattr(ast, 'right', None)
        if isinstance(node, If):
            # only for test
            if node.bool_value(left.eval(env)):
                if_result = sh_eval_list(right, env)
                node.set_result(if_result)
        elif isinstance(node, While):
            while node.bool_value(left.eval(env)):
                while_result = sh_eval_list(right, env)
                node.set_result(while_result)
    return node.eval(env)
