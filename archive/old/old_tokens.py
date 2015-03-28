# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/1/26'


class NumberToken(object):
    def __init__(self, value):
        if '.' in value:
            self.value = float(value)
        else:
            self.value = int(value)

    def nud(self):
        return self

    def __repr__(self):
        return "(number {})".format(self.value)


class AddOpToken(object):
    lbp = 10
    def nud(self):
        # return expression(100)
        self.left = None
        self.right = expression(100)

    def led(self, left):
        self.left = left
        self.right = expression(10)
        return self

    def __repr__(self):
        return "(add {} {})".format(self.left, self.right)


class SubOpToken(object):
    lbp = 10
    def nud(self):
        # return -expression(100)
        self.left = expression()
        self.right = None

    def led(self, left):
        # right = expression(10)
        self.left = left
        self.right = expression(10)
        return self

    def __repr__(self):
        return "(sub {} {})".format(self.left, self.right)


class EndToken(object):
    lbp = 0

    def __repr__(self):
        return "(end)"