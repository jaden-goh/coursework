import tensorflow as tf

# Define the 3x3 checkerboard input
# Shape: (batch_size, height, width, channels)
x = tf.constant([[[[0.0], [1.0], [0.0]],
                  [[1.0], [0.0], [1.0]],
                  [[0.0], [1.0], [0.0]]]], dtype=tf.float32)

# Define the 2x2 kernel initialized at 0.1, no bias
kernel = tf.Variable(tf.ones((2, 2, 1, 1)) * 0.1)

# Target output
y_true = tf.constant([[1.0]])

# Forward and backward pass
with tf.GradientTape() as tape:
    # Watch kernel
    tape.watch(kernel)

    # Convolution (no padding, stride 1)
    conv = tf.nn.conv2d(x, kernel, strides=1, padding='VALID')

    # Apply sigmoid activation
    a = tf.nn.sigmoid(conv)

    # Flatten and pass through a single logistic unit (weights = 1, bias = 0)
    logistic_input = tf.reduce_sum(a)  # equivalent to dot with weights = 1
    y_pred = tf.nn.sigmoid(logistic_input)

    # Simplified squared error loss
    loss = 0.5 * tf.square(y_pred - y_true)

# Compute gradients
grads = tape.gradient(loss, kernel)

print("Predicted y:", y_pred.numpy())
print("Loss:", loss.numpy())
print("Gradients for kernel weights:\n", grads.numpy())
