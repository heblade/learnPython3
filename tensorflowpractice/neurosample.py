import tensorflow as tf

#声明变量
#w1: 2*3矩阵
w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
#b1: [0 0 0] 向量
b1 = tf.Variable(tf.constant(0.0, shape=[3]))
#w2: 3*1矩阵 （3行1列）
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))
#b2: [0]向量
b2 = tf.Variable(tf.constant(0.0, shape=[1]))

#暂时将输入的特征向量定义为一个常量。注意这里x是一个1*2的矩阵
x = tf.constant([[0.7, 0.9]])

#实现神经网络的前向传播过程，并计算神经网络的输出
#a: 1*2 矩阵 x 2*3矩阵 = 1 * 3 矩阵
a = tf.nn.relu(tf.matmul(x, w1)+b1)
#y: 1 * 3矩阵 x 3 * 1矩阵 = 1 * 1矩阵 （即得到一个数)
y = tf.nn.relu(tf.matmul(a, w2)+b2)

with tf.Session() as sess:
    #运行变量初始化过程
    init_op = tf.global_variables_initializer()
    sess.run(init_op)
    print("w1: ", sess.run(w1))
    print("b1: ", sess.run(b1))
    print("w2: ", sess.run(w2))
    print("b2: ", sess.run(b2))
    print("第一层:", sess.run(a))
    print("第二层:", sess.run(y))
