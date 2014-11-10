#coding: utf-8

import re
from collections import namedtuple
from sys import stdin

op_token_map = {'+':'ADD','-':'SUB','*':'MUL','/':'DIV'}
bi_op_token_map = {'ADD':'+', 'SUB': '-', 'MUL': '*', 'DIV':'/'}
Token = namedtuple('Token',('name', 'value'))

pattern = r'[\d.]+|[%s]' % '\\'.join(op_token_map)
pat = re.compile(pattern)

string = stdin.readline()
parts = pat.findall(string)

tokens = [Token(op_token_map.get(x, "NUM"), x) for x in parts]
rule_map = {
        'expr': ['term ADD expr', 'term SUB expr', 'term'],
        'term': ['factor MUL term', 'factor DIV term', 'factor'],
        'factor': ['NUM']
        }

Node = namedtuple('Node', ('name', 'left', 'node', 'right'))

def match(rule_name, tokens):
    rules = rule_name.split()
    if len(rules) == 3:
        if len(tokens) < 3:
            return False, '', tokens, None ,"", [], rule_name
        _rules = filter(lambda rule: rule in rule_map, rules)
        left_rule, right_rule = _rules
        node_rule = filter(lambda rule: rule not in _rules, rules)[0]
        for index, token in enumerate(tokens):
            if token.name in bi_op_token_map:
                node = token
                left_tokens = tokens[:index]
                right_tokens = tokens[index+1:]
                if node.name == node_rule:
                    return True, left_rule, left_tokens, node, right_rule, right_tokens, node_rule
                else:
                    return False, "", tokens, None, "", [], node_rule
    elif len(rules) == 1:
        rule = rules[0]
        return True, "", [], tokens, "", [], rule
        

def build_AST(rule_name, tokens):
    # end
    if not tokens:
        return False, None
    # terminal symbol
    elif rule_name not in rule_map:
        token_name = tokens[0].name
        if token_name == token_name:
            return True, tokens[0]
        else:
            return False, tokens[0]
    # nonterminal symbol
    # productions
    rules = rule_map[rule_name]
    print rules
    for rule in rules:
        matched, left_rule, left_tokens, node, right_rule, right_tokens, node_rule = match(rule, tokens)
        if matched:
            if left_tokens:
                lret, left_node = build_AST(left_rule, left_tokens)
                rret, right_node = build_AST(right_rule, right_tokens)
                if lret and rret:
                    return True, Node(node_rule, left_node, node, right_node)
            else:
                return build_AST(node_rule, node)
    return False, None

print build_AST('expr', tokens)
