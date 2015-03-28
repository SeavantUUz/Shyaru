#coding:utf-8

from sys import stdin
import re

add = re.compile(r'\+')
sub = re.compile(r'-')
div = re.compile(r'/')
mul = re.compile(r'\*')

number = re.compile(r'[1-9][0-9]*|0|[0-9]+\.[0-9]*')

def OP(op,name,stream):
    print stream
    t = op.match(stream)
    if t:
        start, end = t.span() 
        stream = stream[end:]
        return (name,), stream
    else:
        return None, stream

def ADD(stream):
    return OP(add, "ADD", stream)

def SUB(stream):
    return OP(sub, "SUB", stream)

def MUL(stream):
    return OP(mul, "MUL", stream)

def DIV(stream):
    return OP(div, "DIV", stream)

def NUMBER(stream):
    t = number.match(stream)
    if t:
        start,end = t.span()
        print start,end
        value = float(stream[start:end])
        print value
        stream = stream[end:]
        print stream
        return ('DOUBLE_LITERAL',value,stream)
    else:
        return None, stream

temp = None
while temp is None or len(temp):
    temp = stdin.readline()
    while len(temp):
        t = NUMBER(temp)
        if t[0] is not None:
            print t[0]
            temp = t[1]
        t = ADD(temp)
        if t[0] is not None:
            print t[0]
            temp = t[1]
        t = SUB(temp)
        if t[0] is not None:
            print t[0]
            temp = t[1]
        t = MUL(temp)
        if t[0] is not None:
            print t[0]
            temp = t[1]
        t = DIV(temp)
        if t[0] is not None:
            print t[0]
            temp = t[1]
