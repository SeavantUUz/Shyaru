# coding: utf-8
import parser

__author__ = 'AprocySanae'
__date__ = '15/1/16'

with open("/Users/aprocysanae/Github/Shyaru/test/test.shy", 'r') as f:
    print parser.parser(f.read())