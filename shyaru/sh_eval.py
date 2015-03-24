# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/2/28'

from evaluations.factory import typeFactory
from environment import Environment

def sh_eval(ast, env=None):
    if env is None:
        env = Environment()
    if ast is None:
        return None
    Node = typeFactory(ast.id)
    if not Node:
        raise SyntaxError('Unsupported Type: {}'.format(ast.id))
    # 已经到了endpoint
    if not getattr(ast, 'left', None) and not getattr(ast, 'right', None):
        node = Node(ast.value)
        return node
    node = Node()
    left = sh_eval(getattr(ast, 'left', None), env)
    if left is not None:
        node.set(left)
    right = sh_eval(getattr(ast, 'right', None), env)
    if right is not None:
        node.set(right)
    return node.eval(env)
