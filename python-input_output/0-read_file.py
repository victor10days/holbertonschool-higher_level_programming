#!/usr/bin/python3

'''Reads a text file (UTF8) and prints it to sdtout'''


def read_file(filename=''):
    with open('my_file_0.txt', 'r', encoding='utf-8') as f:
        print(f.read(), end='')
