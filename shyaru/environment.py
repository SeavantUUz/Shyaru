# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/3/8'

__all__ = ['Environment']

class Environment(object):
    def __init__(self, parent=None):
        self.context = dict()
        self.parent = parent

    def set(self, name, value):
        try:
            target_context = self.search_name(name)
        except KeyError:
            self.context[name] = value
        else:
            target_context[name] = value
        return value

    def get(self, name, lookup=True):
        try:
            if lookup:
                target_context = self.search_name(name)
                value = target_context[name]
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

    def delete(self):
        if self.parent:
            delattr(self.parent, 'child')
        else:
            del(self)

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
            # return self.context[name]
            return self.context

    def __str__(self):
        return self.context.__str__()