# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '14/12/28'

import re

_number = r'([0-9]+(\.[0-9]+)?)'

_keywords = ['==', '>=', '<=', '\+', '\-', '\*', '\/', '\%', '\(', '\)', '=', '<', '>', '\{', '\}', '\:']

_identify = r'([A-Z_a-z][A-Za-z0-9_]*|{})'.format('|'.join(_keywords))

print _identify

_string = r'([\'\"](.*)[\'\"])'

_rules = [_number, _identify, _string]


pattern = re.compile('|'.join(_rules))

if __name__ == "__main__":
    with open("test.as") as f:
        for line in f:
            for i in pattern.finditer(line):
                print i.group(1)
            # print pattern.findall(line)