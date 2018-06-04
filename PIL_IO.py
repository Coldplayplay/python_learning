# _*_ coding:utf-8 _*_

import Image

im = Image.open("/home/cbc/图片/beauty/DSC_9438.JPG")
w,h = im.size
print w,h

# im.thumbnail((400, 300))
# im.save("/home/cbc/图片/beauty/a1.jpg", 'jpeg')

im_resize = im.resize((4000, 2500))
im_resize.save("/home/cbc/图片/beauty/a3.jpg", 'jpeg')
