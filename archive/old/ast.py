# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/1/3'

class ASLeaf(object):
    def __init__(self, t):
        self.token = t

    def token(self):
        return self.token

    def num_child(self):
        return 0

    def text(self):
        return self.token.get_text()


class ASTList(object):
    def __init__(self, t_list):
        self.children = t_list

    def child(self, i):
        return self.children[i:i+1]

    def children(self):
        return self.children

    def num_child(self):
        return len(self.children)

    def text(self):
        return ",".join([token.get_text() for token in self.children])


class BinaryExpr(ASTList):
    def __init__(self, t_list):
        super(BinaryExpr, self).__init__(t_list)

    def left(self):
        return self.child(0)

    def operator(self):
        return self.child(1)

    def right(self):
        return self.child(2)

