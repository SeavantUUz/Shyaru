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
import inspect


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


def statement():
    global token
    t = token
    if getattr(t, 'std', None):
        advance()
        return t.std()
    v = expression(0)
    advance(';')
    return v


def statements():
    s_list = []
    while True:
        if token.id == '}' or token.id == '(end)':
            break
        v = statement()
        if v:
            s_list.append(v)
    if not s_list:
        return None
    else:
        return s_list[0] if len(s_list) == 1 else s_list


def block():
    global token
    t = token
    advance('{')
    return t.std()


def _tokenize(text):
    f = StringIO(text)
    scope = this['scope']
    for token_type, token_value, _, _, _ in generate_tokens(f.readline):
        #scope = this['scope']
        if token_type == tokenize.NUMBER:
            symbol = scope('(number)')
            s = symbol()
            s.value = int(token_value)
            yield s
        elif token_type ==  tokenize.OP:
            symbol = scope(token_value)
            yield symbol()
        elif token_type == tokenize.STRING:
            symbol = scope('(string)')
            s = symbol()
            s.value = token_value
            yield s
        elif token_type == tokenize.NAME:
            symbol = scope(token_value, auto_commit=False)
            if symbol is None:
                symbol = scope('(name)')
                s = symbol()
                s.value = token_value
            else:
                s = symbol()
            yield s
        elif token_type == tokenize.ENDMARKER:
            break
        else:
            raise SyntaxError("Unknown Operator")
    yield scope('(end)')()


def _parser(program):
    global  token, next
    next = _tokenize(program).next
    token = next()
    return expression()


def parser(program):
    global token, next
    next = _tokenize(program).next
    token = next()
    r_list = statements()
    return r_list


class Token(object):
    id = None
    value = None
    left = None
    right = None
    extra = None
    lbp = None
    def nud(self):
        raise SyntaxError("Syntax Error: {}".format(self.id))

    def led(self, left):
        raise SyntaxError("Unknown Operator: {}".format(self.id))

    def __repr__(self):
        if self.id == '(number)' or self.id == '(string)' or self.id == '(name)':
            return '({} {})'.format(self.id[1:-1], self.value)
        if self.id == '(constant)':
            return '{}'.format(self.value)
        else:
            if self.extra:
                return "({} {} {} {})".format(self.id, self.left, self.right, self.extra)
            else:
                return "({} {} {})".format(self.id, self.left, self.right)


class environment(object):
    def __init__(self, parent=None):
        self.env = dict()
        self.parent = parent
        self.child = None

    def __call__(self, identify, bp=0, auto_commit = True, search = True):
        s = self.env.get(identify)
        if not s:
            if search:
                s = self._search_identify(identify)
            if not s:
                class s(Token):
                    pass
                if auto_commit:
                    s.__name__ = 'symbol-{}'.format(identify)
                    s.id = identify
                    s.lbp = bp
                    self.env[identify] = s
                else:
                    s = None
            else:
                s.lbp = max(s.lbp, bp)
        else:
            s.lbp = max(s.lbp, bp)
        return s

    def _search_identify(self, identify):
        if not self.parent:
            return None
        else:
            parent = self.parent
            value = parent.env.get(identify)
            if value:
                return value
            else:
                return parent._search_identify(identify)

    def fork_env(self):
        _new_env = type(self)(self)
        self.child = _new_env
        return _new_env



this = dict()
this['scope'] = environment()

def infix(identify, bp):
    def led(self, left):
        self.left = left
        self.right = expression(bp)
        return self
    scope = this['scope']
    scope(identify, bp).led = led


def prefix(identify, bp):
    def nud(self):
        self.left = expression(bp)
        self.right = None
        return self
    scope = this['scope']
    scope(identify).nud = nud


def infix_r(identify, bp):
    def led(self, value):
        self.left = value
        self.right = expression(bp - 1)
        return self
    scope = this['scope']
    scope(identify, bp).led = led


def init_rule():
    scope = this['scope']
    scope('(number)').nud = lambda self: self
    scope('(string)').nud = lambda self: self
    scope('(name)').nud = lambda self: self
    scope('(end)')
    infix_r('=', 20)
    infix_r('or', 30)
    infix_r('and', 40)
    prefix('not', 50)
    infix('!=', 60)
    infix('==', 60)
    infix('<', 60)
    infix('>', 60)
    infix('>=', 60)
    infix('<=', 60)
    infix('+', 70)
    infix('-', 70)
    infix('*', 80)
    infix('/', 80)
    infix('%', 80)
    prefix('+', 100)
    prefix('-', 100)
    infix_r('**', 120)
    scope('.', 130)
    scope('[', 130)
    scope('(', 130)
    scope(')')
    scope(']')
    scope('if')
    scope('while')
    scope('else')
    scope('var')
    scope('return')
    scope('function')
    constant('True')
    constant('False')
    constant('None')


def advance(id=None):
    global token
    if id and token.id != id:
        raise SyntaxError("Expect %r" % id)
    token = next()


def method(identify):
    scope = this['scope']
    s = scope(identify)
    assert issubclass(s, Token)
    def bind(func):
        setattr(s, func.__name__, func)
    return bind


def constant(identify):
    @method(identify)
    def nud(self):
        self.id = '(constant)'
        self.value = identify
        return self


@method('(')
def nud(self):
    expr = expression()
    advance(')')
    return expr


@method('.')
def led(self, left):
    if token.id != '(name)':
        raise SyntaxError("Excepted a attribute name")
    self.left = left
    self.right = token
    advance()
    return self


@method('[')
def led(self, left):
    self.left = left
    self.right = expression()
    advance(']')
    return self


@method('{')
def std(self):
    scope = this['scope']
    this['scope'] = scope.fork_env()
    value = statements()
    this['scope'] = scope
    advance('}')
    return value


@method('var')
def std(self):
    global token
    n = token
    if n.id != '(name)':
        raise SyntaxError("Excepted a variable name")
    scope = this['scope']
    scope(n.value, search=False)
    advance()
    if token.id == '=':
        t = token
        t.left = n
        advance('=')
        t.right = expression(0)
        return t
    else:
        raise SyntaxError("Excepted an assignment expression")


@method('if')
def std(self):
    advance('(')
    self.left = expression(0)
    advance(')')
    self.right = block()
    if token.id == 'else':
        advance('else')
        self.extra = block()
    return self


@method('while')
def std(self):
    advance('(')
    self.left = expression(0)
    advance(')')
    self.right = block()
    return self


@method('return')
def std(self):
    if token.id != ';':
        self.left = expression(0)
    advance(';')
    if token.id != '}':
        raise SyntaxError('Excepted brace')
    return self


@method('function')
def std(self):
    t = token
    if t.id != '(name)':
        raise Exception('Error function name')
    scope = this['scope'].fork_env()
    args_list = []
    advance()
    advance('(')
    while True:
        if token.id == ')':
            break
        if token.id != '(name)':
            raise SyntaxError('Excepted args name')
        args_list.append(token)
        scope(token, search=False)
        advance()
        if token.id == ',':
            advance()
    advance(')')
    self.left = t
    self.right = args_list
    self.extra = block()
    return self


@method('(')
def led(self, left):
    self.left = left
    args_list = []
    while True:
        if token.id == ')':
            break
        args_list.append(expression())
        if token.id != ',':
            break
        advance(',')
    advance(')')
    self.right = args_list
    return self


if __name__ == '__main__':
    init_rule()
    print parser("'hello'+'world' + 1;")
    print parser("1*4+5*4;")
    print parser("1*(4+5)*4;")
    print parser("(1*4)+(5*4);")
    a = parser("a = True = False or None;")
    b = parser('a=True;b=False;c;')
    c = parser('if (a==b) {c;}')
    print c
    print parser('function haha(a,b,c) { d; }')

