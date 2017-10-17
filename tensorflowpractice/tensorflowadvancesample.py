import tensorflow as tf
import numpy as np

#使用NumPy生成假数据(phony data)，总共100个点
#随机输入 2 * 100矩阵
x_data = np.float32(np.random.rand(2, 100))
#通过1*2矩阵与2*100矩阵相乘，得到1*100矩阵结果，每一项结果+0.4
y_data = np.dot([0.300, 0.400], x_data) + 0.400

print("x_data: ", x_data)
print("y_data: ", y_data)

#构造一个线性模型
b = tf.Variable(tf.zeros([1]))
W = tf.Variable(tf.random_uniform([1,2], -1.0, -1.0))
y = tf.matmul(W, x_data) + b

#最小化方差
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

#初始化变量
init = tf.initialize_all_variables()

#启动图
with tf.Session() as sess:
    sess.run(init)
    print("b: ", sess.run(b))
    print("W: ", sess.run(W))
    print("y: ", sess.run(y))
    print("loss: ", sess.run(loss))
    print("train: ", sess.run(train))
    for step in range(0, 401):
        sess.run(train)
        if step % 20 == 0:
            print("step: ", step, "W: ", sess.run(W), "b: ", sess.run(b))