# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/2/27'

from parser import parser, init_rule
from sh_eval import sh_eval
init_rule()

ast = parser('1+2.0;')
print ast
print sh_eval(ast)
print sh_eval(parser('1+2+6;'))