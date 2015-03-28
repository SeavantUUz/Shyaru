__author__ = 'aprocysanae'
#coding: utf-8
import re

from abc import ABCMeta, abstractmethod

class Token(object):
    EOL = '\n'
    def __init__(self, line_number):
        self.current_line = line_number

    def is_identifier(self):
        return False

    def is_number(self):
        return False

    def is_string(self):
        return False

    def get_current_line(self):
        return self.current_line

    def get_number(self):
        raise Exception("Not a number token")

    def get_text(self):
        raise Exception("Not a string token")


class NumberToken(Token):
    def __init__(self, line, number):
        if not '.' in number:
            self.value = int(number)
        else:
            self.value = float(number)
        super(NumberToken, self).__init__(line)

    def is_number(self):
        return True

    def get_number(self):
        return self.value

    def get_text(self):
        return str(self.value)

    def __str__(self):
        return "Number:{}".format(self.value)

    def __repr__(self):
        return "{}".format(self.value)


class StringToken(Token):
    def __init__(self, line, text):
        self.value = text
        super(StringToken, self).__init__(line)

    def is_string(self):
        return True

    def get_text(self):
        return self.value

    def __str__(self):
        return "String:{}".format(self.value)

    def __repr__(self):
        return "{}".format(self.value)

class IdToken(Token):
    def __init__(self, line, id_):
        self.value = id_
        super(IdToken, self).__init__(line)

    def is_identifier(self):
        return True

    def get_text(self):
        return self.value

    def __str__(self):
        return "Id:{}".format(self.value)

    def __repr__(self):
        return "{}".format(self.value)
