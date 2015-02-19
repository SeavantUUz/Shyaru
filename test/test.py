# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/1/16'

from tokenize import generate_tokens
from cStringIO import StringIO

with open('test.as', 'r') as f:
    for i in generate_tokens(f.readline):
        print i
