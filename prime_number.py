#判断一个数是否为质数
#用1至n-1去除n，判断能否整除

n = int(input('请输入一个数字n：'))
m = 0
if n <= 3:
    print ('n是质数')
else:
    for i in range(2,n-1):
        if n % i == 0:
            m = m + 1
            break
if m > 0:
     print('%d不是质数' % int(n))
else:
    print('%d是质数' % int(n))


