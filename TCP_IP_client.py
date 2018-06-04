# _*_ coding: utf-8 _*_
#导入socket库
import socket
#创建一个socket,定义IPv4,以及TCP的协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立连接,给出IP和端口号
s.connect(('127.0.0.1', 9999))
print 'success connect to 127.0.0.1.'
print s.recv(1024)

names = ['cbc','yjy','dbb']
for name in names:
    s.send(name)
    print s.recv(1024)
#关闭连接
s.close()
