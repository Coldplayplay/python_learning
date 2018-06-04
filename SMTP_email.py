# _*_ coding: utf-8 _*_
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = '239240929@qq.com'
password = 'nuikoksbahdjbidc' #授权码
smtp_server = 'smtp.qq.com'
to_addr = 'yangjianye728@126.com'

# 邮件对象:
msg = MIMEMultipart()
msg['From'] = _format_addr(u'小仙女 <%s>' % from_addr)
msg['To'] = _format_addr(u'亲爱的 <%s>' % to_addr)
msg['Subject'] = Header(u'来自我的问候...嘿嘿嘿', 'utf-8').encode()

# 邮件正文是MIMEText:
#msg = MIMEText('hello baby, guess who am I.——send by Python', 'plain', 'utf-8')
msg_text = MIMEText('<html><body><h1>Hello, Baby</h1>' +
'<p>send by <a href="http://www.python.org">Python</a>...</p>' + '</body></html>', 'html', 'utf-8')
msg.attach(msg_text)

# 添加附件就是加上一个MIMEBase,从本地读取一个图片:
with open('/home/cbc/DL/fast-neural-style-master/1_wave.png', 'rb') as f:
    # 设置附件的MIME和文件名,这里是png类型:
    mime = MIMEBase('image', 'png', filename='wangzi.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='wangzi.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)
with open('/home/cbc/图片/beauty/2.jpeg', 'rb') as f:
    # 设置附件的MIME和文件名,这里是png类型:
    mime = MIMEBase('image', 'jpeg', filename='gongzhu.jpeg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='gongzhu.jpeg')
    mime.add_header('Content-ID', '<1>')
    mime.add_header('X-Attachment-Id', '1')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP_SSL(smtp_server) # SMTP协议默认端口是25. 465/587是腾讯qq邮箱的smtp服务器端口
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

