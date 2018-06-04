import os
import sys

def search(name, dir = '.'):
    for x in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, x)) and name in x:
            print os.path.join(dir, x)[2:]
        elif os.path.isdir(os.path.join(dir, x)):
            search(name, os.path.join(dir, x))


if __name__ == '__main__':
    x = 1
    search('test')