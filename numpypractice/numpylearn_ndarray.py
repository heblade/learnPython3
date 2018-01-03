import numpy as np

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print("b is ", b,
      "\nc is ", c,
      "\ndtype of c is ", c.dtype,
      "\na.shape is ", a.shape,
      "\nc.shape is ", c.shape)

c.shape = (4,3)
print("c is ", c)

#当某个轴的元素为-1时，将根据数组元素的个数自动计算轴的长度
c.shape = (2, -1)
print("c is ", c)

c.shape = (3, -1)
print("c is ", c)

#使用数组的reshape方法，可以创建一个改变了尺寸的新数组，原数组的shape保持不变
d = a.reshape(2,2)
print("d is ", d,
      "\na is ", a)

#a与d共享数据存储内存区域，因此修改其中任意一个数组的元素都会同时修改另外一个数组的内容
a[1] = 100
print("d is ", d,
      "\na is ", a)

e = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]], dtype=np.float)
print("e is ", e)

f = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]], dtype=np.complex)
print("f is ", f)

rangesample = np.arange(0, 1, 0.1)
print("range sample is ", rangesample)

linspacesample = np.linspace(0, 1, 12)
print("linspace sample is ", linspacesample)

#logspace, 第一个参数:0，代表起始数为10^0 = 1；第二个参数:2，代表最大值：10^2 = 100
logspacesample = np.logspace(0, 2, 20)
print("logsapce sample is ", logspacesample)

s = "abcdefgh"
#如果从字符串s创建一个8bit的整数数组的话，
#所得到的数组正好就是字符串中每个字符的ASCII编码
print(np.fromstring(s, dtype=np.int8))

#两个相邻的字节就表示一个整数，
#把字节 98 和字节 97 当作一个 16 位的整数，它的值就是 98*256+97 = 25185。
#可以看出内存中是以 little endian(低位字节在前)方式保存数据的
print(np.fromstring(s, dtype=np.int16))

def func(i):
    return i % 4 + 1

#fromfunction 函数的第一个参数为计算每个数组元素的函数，第二个参数为数组
#的大小(shape)，因为它支持多维数组，所以第二个参数必须是一个序列，本例
#中用(10,)创建一个 10 元素的一维数组
print("np.fromfunction: ", np.fromfunction(func, (10,)))

def ninexnine(i, j):
    return (i + 1) * (j + 1)
print("9x9 table: ", "\n", np.fromfunction(ninexnine, (9, 9)))
