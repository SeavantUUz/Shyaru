# coding: utf-8
__author__ = 'AprocySanae'
__date__ = '14/12/29'

from rules import pattern
from token import IdToken, NumberToken, StringToken

class Lexer(object):
    def __init__(self):
        self.current_line = 0
        self.tokens = []

    def readline(self, line):
        self.current_line += 1
        # tokens = pattern.findall(line)
        for token in pattern.finditer(line):
            if token.group(1):
                self.tokens.append(NumberToken(self.current_line, token.group(1)))
            elif token.group(3):
                self.tokens.append(IdToken(self.current_line, token.group(3)))
            elif token.group(5):
                self.tokens.append(self.current_line, StringToken(token.group(5)))

    def peek(self, n):
        if self.tokens:
            return None
        return self.tokens[:n]

    def read(self):
        if self.tokens:
            return None
        item = self.tokens[0]
        del self.tokens[0]
        return item

if __name__ == '__main__':
    lexer = Lexer()
    with open("test.as") as f:
        for line in f:
            lexer.readline(line)
    print lexer.tokens
