# -*- coding:utf-8 -*-
def greet(name):
    print(u'hello, ', name, u'!')
    greet2(name)
    print(u'getting ready to say bye...')
    bye()

def greet2(name):
    print(u'how are you, ', name, u'?')

def bye():
    print(u'ok bye!')

greet('Maggie')
