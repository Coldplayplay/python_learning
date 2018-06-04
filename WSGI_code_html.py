# _*_ coding: utf-8 _*_
#实现Web应用程序的WSGI处理函数
def appliction(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1> Hello, %s!</h1>' %(environ['PATH_INFO'][1:] or 'Web')

#启动WSGI服务器，加载application函数
from wsgiref.simple_server import make_server

#创建一个服务器，IP地址为空，端口是8000，处理函数是application
httpd = make_server('', 8000, appliction)
print 'Serving HTTP on port 8000...'
#开始监听HTTP请求
httpd.serve_forever()