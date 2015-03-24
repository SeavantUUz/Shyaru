# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/2/27'

from parser import parser, init_rule
from sh_eval import sh_eval
init_rule()

import time
start_time = time.time()
# print sh_eval(parser('1+2+3+4+5+6+6;'))
# print sh_eval(parser('1+3/2+4;'))
print sh_eval(parser('"hello" + "world";'))
print time.time() - start_time
print sh_eval(parser('1+2+6;'))
# print sh_eval(parser('1-2-2*6+6*2;'))
# print sh_eval(parser("'hello '  + 'world';"))
#
with open('/Users/aprocysanae/Github/Shyaru/test/test1.shy') as f:
    for line in f:
        print sh_eval(parser(line))