# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/2/28'


def evaluate(ast, env=None):
    if env is None:
        env = environment()
    return ast.eval(env)


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
    return env[self.value]


def assign_evaluate(self, env):
    if self.left.id != '(name)':
        raise SyntaxError("can't assign to wrong type")
    right = evaluate(self.right, env)
    env[self.left.value] = right
    return right


