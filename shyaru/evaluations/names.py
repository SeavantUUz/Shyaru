# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/3/15'


def name_evaluate(self, env, value_type):
    result = env.get(self.value)
    if result is None:
        raise SyntaxError("name '{}' is not defined".format(self.value))
    return result


def init_eval():
    r = dict()
    r['(number)'] = name_evaluate
    return r