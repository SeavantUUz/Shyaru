# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/4/4'

from ..evaluations import Base

class If(Base):
    def __init__(self):
        super(If, self).__init__()
        self.instant_eval = False

    def eval(self, env):
        return type(self)()

    def __str__(self):
        return 'if'

