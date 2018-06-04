# _*_ coding:utf-8 _*_

'''
ThreadLocal
1.threading.local()创建全局变量比如local_school，
2.但每个属性如 local_school.student都是线程的局部变量,
可以任意读写而互不干扰,也不用管理锁的问题, ThreadLocal 内部会处理。

最常用的地方就是为每个线程绑定一个数据库连接,HTTP请求,用户身份信息等,这样一个线程的所
有调用到的处理函数都可以非常方便地访问这些资源。
'''

import threading
# 创建全局ThreadLocal对象:
local_school = threading.local()
def process_student():
    print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)
def process_thread(name):
    local_school.student = name #属性是每个线程的局部变量
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()