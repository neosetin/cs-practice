import numpy as np

#задание 1

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print(hours)
print(hours.shape, hours.ndim, hours.size, hours.dtype)
print()

#задание 2

print(hours.item(2))
print(hours[-1])
print(hours[2:6])
print(hours[::2])
print(hours[::-1])
print()

#задание 3

temperatures = np.array([
    list((12, 14, 13, 15)),
    list((11, 13, 16, 17)),
    list((10, 12, 15, 18))
])

print(temperatures.shape, temperatures.ndim, temperatures.size)
print(temperatures[1, 2])
print(temperatures[0])
print(temperatures[:, -1])
print(temperatures[:2, 1:])

center = temperatures[:2, 1:3]
print(center)
print()

#задание 4

matrix = np.arange(1, 26).reshape(5, 5)

part1 = matrix[:3]
print(part1)
print(part1.shape)

part2 = matrix[-2:]
print(part2)
print(part2.shape)

part3 = matrix[:, :2]
print(part3)
print(part3.shape)

part4 = matrix[1:4, 2:5]
print(part4)
print(part4.shape)

part5 = matrix[-2:, -2:]
print(part5)
print(part5.shape)
print()

#задание 5

vector = np.array(list((10, 20, 30, 40, 50)))
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1

print(changed_hours)
print(hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print(changed_matrix)
print(matrix)
print()

#задание 6

numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print(numbers.shape)
print(table.shape)
print(transposed.shape)
