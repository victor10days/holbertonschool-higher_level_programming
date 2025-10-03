#!/usr/bin/python3
'''Appends a string at the end of a UTF8 and returns number of characters'''


def append_write(filename='', text=''):
	with open (filename, 'a', encoding='utf-8') as f:
		return f.append_write(text)
