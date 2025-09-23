import numpy as np

A = np.array([10, 20, 30, 40, 50])
B = np.array([5, 4, 3, 2, 1])
sum_ab = A + B
print("Sum of A and B:", sum_ab)
sum_ab = A - B
print("Subtraction of B from A:", sum_ab)
mul_ab = A * B
print("Element-wise multiplication:", mul_ab)
div_ab = A / B
print("Division of A by B:", div_ab)
mean_a = np.mean(A)
max_a = np.max(A)
min_a = np.min(A)
print("Mean of A:", mean_a)
print("Maximum of A:", max_a)
print("Minimum of A:", min_a)
dot_product_ab = np.dot(A, B)
print("Dot product of A and B:", dot_product_ab)
reshaped_a = A.reshape(5, 1)
print("Reshaped A (5x1 matrix):\n", reshaped_a)