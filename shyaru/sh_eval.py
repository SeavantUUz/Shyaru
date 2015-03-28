# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/2/28'

__all__ = ['sh_eval']

from .evaluations.factory import typeFactory
from .environment import Environment
from .evaluations.names import Name

def sh_eval(env=None):
    variable = {'env': env}
    def _sh_eval(ast, env=None):
        if env is None:
            if variable['env'] is None:
                env = Environment()
            else:
                env = variable['env']
        else:
            env = env
        if ast is None:
            return None
        Node = typeFactory(ast.id)
        if not Node:
            raise SyntaxError('Unsupported Type: {}'.format(ast.id))
        # 已经到了endpoint
        if not getattr(ast, 'left', None) and not getattr(ast, 'right', None):
            node = Node(ast.value)
            if type(node) == Name:
                try:
                    node = env.get(ast.value)
                except NameError:
                    node = node
            return node
        node = Node()
        left = _sh_eval(getattr(ast, 'left', None), env)
        if left is not None:
            node.set(left)
        right = _sh_eval(getattr(ast, 'right', None), env)
        if right is not None:
            node.set(right)
        return node.eval(env)
    return _sh_eval
