# ‐*‐ coding: utf‐8 ‐*‐

##接受用户输入
#name = raw_input("Please say your name:")
#print 'hello,', name

def sum_square(*nums):
    sum = 0
    for num in nums:
        sum += num*num

    return sum

##递归 容易发生栈溢出
def fact(n):
    if n==1:
        return 1
    return fact(n-1)*n

##尾递归 始终只占一个栈帧 不会出现栈溢出
def fact_wei(n):
    return fact_iter(n, 1)

def fact_iter(n, product):
    if n == 1:
        return product
    return fact_iter(n-1, n*product)

##map和reduce的应用
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

def name_guifan(s):
    temp = ''
    for item in s:
        temp += item.lower()
    return temp[0].upper() + temp[1:]

#t = ['adam', 'LISA', 'barT']
#result = map(name_guifan, t)

def prod(s):
    def mul(x,y):
        return x*y
    return reduce(mul, s)

def is_odd(s):
    return s%2 == 1


def ignore_da_xiao_xie(x, y):
    #a = x.upper()
    #b = y.upper()
    a, b = x, y
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

#b = ['bob', 'about', 'Zoo', 'Credit']

#result = sorted(b)
#result1 = sorted(b, ignore_da_xiao_xie)

#a = [1,2,3,4]
#result = filter(is_odd, a)
#print(result)
#print(result1)


def count():
    fs = []
    for i in range(1, 4):
        def f(i):
            def g():
                return i*i
            return g
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
a,b,c = f1(),f2(),f3()
#print(a,b,c)

#result = map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
#print(result)


def build(x, y):
    return lambda: x * x + y * y
result = build(1,2)


def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper


#@log
def now():
    print '2013-12-25'

#now()


import sys

#print(sys.argv)

class Student(object):
    def __init__(self, name, score, gender='male'):
        self.__name = name
        self.__score = score
        self.gender = gender

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0<=score<=100:
            self.__score = score
        else:
            print('bad score')

    def print_info(self):
        print(self.__name, self.__score)


    def __getattribute__(self, item):
        if item == 'age':
            return 99
        else:
            raise AttributeError('Student class doesn\'t have %s attribute' % item )


class Animal(object):
    def run(self):
        print('Animal is running.')

class Dog(Animal):
    pass

class Cat(Animal):
    pass


def run_twice(animal):
    animal.run()
    animal.run()

"""
定义可迭代的class
__iter__  和 __next__用于for循环
__getitem__用于index获取索引值
"""
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 19:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a+b
            return a
        elif isinstance(item, slice):
            a, b = 1, 1
            start = item.start
            stop = item.stop
            result = []
            for x in range(stop):
                if x >= start:
                    result.append(a)
                a, b = b, a + b
            return result
        else:
            raise TypeError("Only support interger or slice.")

"""
__getattribute__应用
"""
class chain(object):
    def __init__(self, path=''):
        self.__path = path
    def __getattr__(self, item):
        return chain('%s/%s' % (self.__path, item))
    def __str__(self):
        return self.__path


"""
metaclass
"""
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value : self.append(value)
        return type.__new__(cls, name, bases, attrs)

class Mylist(list):
    __metaclass__ = ListMetaclass



if __name__ == '__main__':
    #a = Student('Xiao Ming', 89)
    #print(a.age)
    # a.print_info()
    # a.set_score(99)
    # a.print_info()
    # run_twice(Animal())

    # for i in Fib():
    #     print(i)

    #print(Fib()[:1:5])

    #print(chain().cbc.local.home)

    l = Mylist()
    l.add(112)
    print(l)
