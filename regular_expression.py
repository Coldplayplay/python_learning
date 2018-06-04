# _*_ coding:utf-8 _*_
import re

# if re.match(r'^\d{3}-\d{3,8}$', '010-12345'):
#     print 'ok'
# else:
#     print 'failed'

'''
如果一个正则表达式要重复使用几千次,出于效率的考虑,我们可以预编译该正则表达式,接下来重复使用时就不
需要编译这个步骤了,直接匹配.
'''
tele = re.compile(r'^(\d{3})-(\d{3,8})$')
a = tele.match('010-12345').groups()
b = tele.match('010-123').groups()
#print a,b

'''
Is_Email
'''
email = r'^[a-zA-Z_][0-9a-zA-Z_]*.?[0-9a-zA-Z_]*@[0-9a-z]*.com$'
#[0-9a-z].com
if re.match(email, 'a_1.gates@gmail.com'):
    print 'ok'
else:
    print 'failed'