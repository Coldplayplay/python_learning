# _*_ coding: utf-8 _*_

'''
1如果认为某部分代码可能会出错
 就用try...except...
2可以用多个 except 来捕获不同类型的错误
3此外,如果没有错误发生,可以在 except 语句块后面加一个 else ,
 当没有错误发生时,会自动执行 else 语句
'''
import pdb
import logging
logging.basicConfig(level=logging.DEBUG)
try:
    print 'try...'
    r = 10 / 'a'
    print 'result:', r
# except ZeroDivisionError, e:
#     print 'ZeroDivisionError: ', e
# except ValueError, e:
#     logging.exception(e)
# else:
#     print 'No errors'
finally:
    print('finally')
print 1+2+3+4
print('END.')


def foo(s):
    n = int(s)
    #assert n!=0, 'n is zero'
    return 10 / n
def bar(s):
    #return foo(s)
    try:
         print foo(s) * 2

    except ZeroDivisionError, e:
         # print 'Error!'
         #logging.exception(e)
         raise
    except AssertionError,e:
        print 'AssertionError',e
def main():
    bar('0')
    print 'main is over'
#main()



s = '0'
n = int(s)
#logging.debug('n = %d' % n)
pdb.set_trace()
print 1+2+3
pdb.set_trace()
print 10 / n
