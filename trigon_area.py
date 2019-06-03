
import math

a=int(input('请输入三角形的三边长a:'))
b=int(input('请输入三角形的边长b:'))
c=int(input('请输入三角形的边长c:'))

if a+b>c and a+c>b and b+c>a:
   d=(a+b+c)*(a+b-c)*(a+c-b)*(b+c-a)
   area=1/4*math.sqrt(d)
   print('该三角形面积为:%d' % float(area))
else:
   print('以上三边无法构成一个三角形')
