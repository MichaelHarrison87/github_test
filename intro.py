import tensorflow as tf

x=2
y=4
op1 = tf.add(x,y)
op2 = tf.multiply(x,y)
op3 = tf.pow(op2,op1)

writer = tf.summary.FileWriter('./graphs',tf.get_default_graph())

sess = tf.Session()

print('Answer is:')
print(sess.run(op3))

writer = tf.summary.self.FileWriter('./graphs', sess.graph)

print((x*y)**(x+y))

write.close()
