# _*_ coding:utf-8 _*_

'''
带有lock的例子

1.获得锁的线程用完后一定要释放锁,否则那些苦苦等待锁的线程将永远等待下去,成为死线程。所以我们
用 try...finally 来确保锁一定会被释放
2.锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行,
3.1坏处当然也很多,首先是阻止了多线程并发执行,包含锁的某段代码实际上只能以单线程模式执行,效率就大大地下降了。
3.2其次,由于可以存在多个锁,不同的线程持有不同的锁,并试图获取对方持有的锁时,可能会造成死锁,导致多个线程全部挂起,
既不能执行,也无法结束,只能靠操作系统强制终止。
4.Python存在GIL锁，导致线程不能同步并发
'''
import time, threading
# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()
def change_it(n):
    # 先存后取,结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n
def run_thread(n):
    for i in range(100000):
        lock.acquire()#先要获得锁
        try:
            change_it(n)
        finally:
            lock.release()#最后一定要释放锁
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance