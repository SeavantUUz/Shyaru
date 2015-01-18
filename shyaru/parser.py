# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '15/1/4'

# program: statements
# statements: statement
# block: "{" statement "}" | ""
# statement: "if" expr block ["else" block] | "while" expr block | expr ";"
# expr: factor OP expr
# factor: "-"item | item
# item: "(" expr ")" | NUMBER | IDENTIFIER | STRING

from cStringIO import StringIO
from tokenize import generate_tokens
import tokenize

a = "1 + 2"

def expression(rbp=0):
    global token
    t = token
    token = next()
    left = t.nud()
    while rbp < token.lbp:
        t = token
        token = next()
        left = t.led(left)
    return left


class NumberToken(object):
    def __init__(self, value):
        if '.' in value:
            self.value = float(value)
        else:
            self.value = int(value)

    def nud(self):
        return self.value


class AddOpToken(object):
    lbp = 10
    def led(self, left):
        right = expression(10)
        return left + right


class SubOpToken(object):
    lbp = 10
    def led(self, left):
        right = expression(10)
        return left - right


class EndToken(object):
    lbp = 0


def _tokenize(text):
    f = StringIO(text)
    for token_type, token_value, _, _, _ in generate_tokens(f.readline):
        if token_type == tokenize.NUMBER:
            yield NumberToken(token_value)
        elif token_type ==  tokenize.OP:
            if token_value == '+':
                yield AddOpToken()
            elif token_value == '-':
                yield SubOpToken()
    yield EndToken()


def parser(program):
    global  token, next
    next = _tokenize(program).next
    token = next()
    return expression()


if __name__ == '__main__':
    print parser("1+2-4")

