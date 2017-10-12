###softmax
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

#MNIST数据集相关的常数
#输入层的节点数。对于MNIST数据集，这个就等于图片的像素28x28
INPUT_NODE = 784
#输出层的节点数。这个等于类别的数目。
# 因为在MNIST数据集中，需要区分的是0~9这10个数字，所以这里输出层的节点数为10
OUTPUT_NODE = 10
#学习率
LEARNING_RATE = 0.01
#训练轮数
TRAINING_STEPS = 1000
# 一个训练batch中的训练数据个数。数字越小时，训练过程越接近
# 随机梯度下降；数字越大时，训练越接近梯度下降。
BATCH_SIZE = 100
                        
logpath = '/tmp/mnist_logs'

###prepare data
mnist = input_data.read_data_sets('MNIST_data', one_hot= True)

###create the graph
x = tf.placeholder(tf.float32, shape=[None, INPUT_NODE], name = 'x')
y_ = tf.placeholder(tf.float32, shape=[None, OUTPUT_NODE], name = 'y_')
W = tf.Variable(tf.zeros([INPUT_NODE, OUTPUT_NODE]))
b = tf.Variable(tf.zeros([OUTPUT_NODE]), name= 'input_bias')
y = tf.nn.softmax(tf.matmul(x, W) + b)
tf.summary.histogram('y', y)
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
tf.summary.scalar('loss_function', cross_entropy)
# 使用tf.train.GradientDescentOptimizer优化算法来优化损失函数
train_step = tf.train.GradientDescentOptimizer(LEARNING_RATE).minimize(cross_entropy)
# 检验神经网络的正确率
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float32"))

tf.summary.scalar('accuracy', accuracy)
merged_summary_op = tf.summary.merge_all()

###Cannot evaluate tensor using 'eval()': No default session is registered
###Use 'with sess.as_default()' or pass an explicit session to 'eval(session=sess)'
#set sess as default
# 初始化会话并开始训练过程
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    if tf.gfile.Exists(logpath):
        tf.gfile.DeleteRecursively(logpath)
    summary_writer = tf.summary.FileWriter(logpath, sess.graph)

    for i in range(TRAINING_STEPS):
        batch = mnist.train.next_batch(BATCH_SIZE)
        sess.run(train_step, feed_dict={x:batch[0], y_:batch[1]})
        summary_str = sess.run(merged_summary_op, feed_dict={x: batch[0], y_: batch[1]})
        summary_writer.add_summary(summary_str, i)

        if i%50 == 0:
            print("Step: ", i, "Accuracy: ", sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

    print(accuracy.eval(session=sess, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

### to view result graph by tensorboard, please input below command in cmd window:
### tensorboard --logdir /tmp/mnist_logs/
### then view graph by: http://sz-14m6882:6006