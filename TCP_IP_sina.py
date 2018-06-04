# _*_ coding: utf-8 _*_
#导入socket库
import socket
#创建一个socket,定义IPv4,以及TCP的协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立连接,给出IP和端口号
s.connect(('www.sina.com.cn', 80))
print 'success connect to sina.'
#发送数据：
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#接收数据：
buffer = []
while True:
    #每次最多接收1k字节：
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)

#关闭连接
s.close()

'''
处理数据，接收的数据包括HTTP头和网页本身
我们需要把HTTP头和网页分离一下
打印HTTP头，保存网页内容到文件
'''

header, html = data.split('\r\n\r\n', 1)
print header

with open('sina.html', 'w') as f:
    f.write(html)