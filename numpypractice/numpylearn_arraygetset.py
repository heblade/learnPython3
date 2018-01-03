import numpy as np

a = np.arange(10)
print("a: ", a)
print("a[5]: ", a[5])
# 用范围作为下标获取数组的一个切片，包括 a[3]不包括 a[5]
print("a[3:5]: ", a[3:5])
# 省略开始下标，表示从 a[0]开始,输出至a[4]
print("a[:5]: ", a[:5])
#下标可以用负数，表示数组从后往前数
print("a[:-1]: ", a[:-1])
print("a[:-3]: ", a[:-3])

a[2:4] = 100, 101
print("a: ", a)

# 通过下标范围产生一个新的数组 b， b 和 a 共享同一块数据空间
b= a[3:7]
print("b: ", b)
b[2] = -10
print("b: ", b)
print("a: ", a)

print("使用整数序列")
x = np.arange(10, 1, -1)
print("x: ", x)
print("x[[3, 3, 1, 8]]: ", x[[3, 3, 1, 8]])
newx = x[np.array([3, 3, -3, 8])]
print("newx: ", newx)
newx[2] = 100
print("x: ", x)
print("newx: ", newx)

print('使用布尔数组')
x = np.random.rand(10)
print("x: ", x)
print("x > 0.5 ", x>0.5)
print("x[x>0.5] ", x[x>0.5])

print("多维数组")
multi = np.arange(0, 60, 10).reshape(-1, 1) + np.arange(0, 6)
print(multi)
#row[0]取索引为1的值；row[1]取索引为2的值；row[2]取索引为3的值；
#row[3]取索引为4的值；row[4]取索引为5的值；
print(multi[(0, 1, 2, 3, 4), [1, 2, 3, 4, 5]])

print("矩阵")
matrixa = np.array([[1, 80], [1, 110], [1, 50], [1,60]])
matrixb = np.array([[-40, 200, -150], [2, 0.1, 4]])
print(matrixa, "*", matrixb, " = ", matrixa.dot(matrixb))