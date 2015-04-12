# coding: utf-8
import parser

__author__ = 'AprocySanae'
__date__ = '15/2/27'

from parser import init_rule, parser
from shyaru.sh_eval import sh_eval_list
from shyaru.environment import Environment

init_rule()

import time
start_time = time.time()
# print sh_eval(parser('1+2+3+4+5+6+6;'))
# print sh_eval(parser('1+3/2+4;'))
# env = Environment()
# sh_eval = sh_eval(env)
print parser('"hello" + "world";')
print sh_eval_list(parser('"hello" + " world";'))
# print time.time() - start_time
# print sh_eval_list(parser('1+2+6;'))
# print sh_eval(parser('1-2-2*6+6*2;'))
# print sh_eval(parser("'hello '  + 'world';"))
#
print sh_eval_list(parser('b=1;'))
print sh_eval_list(parser('if (1) {a=1;}'))
# with open('/Users/aprocysanae/Github/Shyaru/test/test1.shy') as f:
#     for line in f:
#         print sh_eval_list(parser(line))