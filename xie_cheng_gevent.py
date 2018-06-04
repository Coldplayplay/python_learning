# _*_ coding: utf-8 _*_

'''
Python通过 yield 提供了对协程的基本支持,但是不完全。而第三方的gevent为Python提供了比较完善的协程支
持。
gevent是第三方库,通过greenlet实现协程,其基本思想是:
当一个greenlet遇到IO操作时,比如访问网络,就自动切换到其他的greenlet,等到IO操作完成,再在适当的时候切
换回来继续执行。由于IO操作非常耗时,经常使程序处于等待状态,有了gevent为我们自动切换协程,就保证总有g
reenlet在运行,而不是等待IO。
由于切换是在IO操作时自动完成,所以gevent需要修改Python自带的一些标准库,这一过程在启动时通过monkey p
atch完成.

当然,实际代码里,我们不会用 gevent.sleep() 去切换协程,而是在执行到IO操作时,gevent自动切换.

从结果看,3个网络操作是并发执行的,而且结束顺序不同,但只有一个线程。

使用gevent,可以获得极高的并发性能,但gevent只能在Unix/Linux下运行,在Windows下不保证正常安装和运
行。
由于gevent是基于IO切换的协程,所以最神奇的是,我们编写的Web App代码,不需要引入gevent的包,也不需要
改任何代码,仅仅在部署的时候,用一个支持gevent的WSGI服务器,立刻就获得了数倍的性能提升。具体部署方式
可以参考后续“实战”­“部署Web App”一节。
'''

from gevent import monkey;monkey.patch_socket();monkey.patch_all()
import gevent
import urllib2

def f(n):
    for i in range(n):
        print gevent.getcurrent(), i
        gevent.sleep(0)

# g1 = gevent.spawn(f1,5)
# g2 = gevent.spawn(f1,5)
# g3 = gevent.spawn(f1,5)
#
# g1.join()
# g2.join()
# g3.join()

def f(url):
    print('GET:%s'%url)
    resp = urllib2.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.'%(len(data), url))

gevent.joinall([gevent.spawn(f, 'http://www.python.org/'),
                gevent.spawn(f, 'http://www.yahoo.com/'),
                gevent.spawn(f, 'http://github.com/'),])
