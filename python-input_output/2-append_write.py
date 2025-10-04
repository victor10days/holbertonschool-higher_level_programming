#!/usr/bin/python3
'''Appends a string at the end of a UTF8 and returns number of characters'''


def append_write(filename='', text=''):
    '''Appends to UTF8 and returns the number of characters written.'''
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
