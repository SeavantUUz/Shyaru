import re
from collections import namedtuple
from sys import stdin

op_token_map = {'+':'ADD','-':'SUB','*':'MUL','/':'DIV'}
Token = namedtuple('Token',('name', 'value'))

pattern = r'[\d.]+|[%s]' % '\\'.join(op_token_map)
pat = re.compile(pattern)

string = stdin.readline()
parts = pat.findall(string)
#print(tokens)
tokens = [Token(op_token_map.get(x, "NUM"), x) for x in parts]
#print(a)
rule_map = {
            'expr': ['term ADD expr', 'term SUB expr', 'term'],
            'term': ['factor MUL term', 'factor DIV term', 'factor'],
            'factor': ['NUM']
            }

RuleMatch = namedtuple('RuleMatch', ('name', 'tokens'))

def to_AST(rule_name, tokens):
    if tokens and rule_name == tokens[0].name:
        return RuleMatch(tokens[0], tokens[1:]) , tokens[1:]
    for rule in rule_map.get(rule_name, []):
        remain_tokens = tokens
        matched_list = []
        for subrule in rule.split():
            matched, remain_tokens = to_AST(subrule, remain_tokens)
            if not matched:
                break
            matched_list.append(matched)
        else:
            return RuleMatch(rule, matched_list), remain_tokens
    return None, None

# simpliest
# Node = namedtuple('Node', ('name', 'token', 'left', 'right'))
# def to_AST(rule_name, tokens):
#     rules = rule_map.get(rule_name,[]) 
#     for rule in rules:
#         subrules = rule.split()
#         for subrule in subrules:
#             if subrule in op_token_map:
#                 for token in tokens:
#                     if token.name == subrule:
#                         return Node(subrule, token, to_AST(left), to_AST(right))
#                 continue
#             else:
#                 
# print(match('expr', tokens))

def print_AST(ast, indent=0):
    rule_match, tokens = ast
    if isinstance(rule_match, RuleMatch):
        rule = rule_match.name
    else:
        rule = rule_match
        rule_match = ast
    # else:
    #     rule = rule_match.name
    if isinstance(rule, Token):
        name = rule.name
        value = rule.value
        print(" " * indent + name + ": " + value)
    else:
        print(" " * indent + rule)
        if not tokens:
            print_AST(rule_match, indent+4)
        for token in tokens:
            print_AST(token, indent+4)

print_AST(to_AST('expr', tokens))
#print to_AST('expr', tokens)

    



