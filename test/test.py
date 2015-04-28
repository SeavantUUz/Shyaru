# coding: utf-8
import parser

__author__ = 'AprocySanae'
__date__ = '15/1/16'

from tokenize import generate_tokens

with open("/Users/aprocysanae/Github/Shyaru/test/test1.shy", 'r') as f:
    for token_type, token_value, _, _, line in generate_tokens(f.readline):
        print token_type, token_value