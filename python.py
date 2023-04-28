import random
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
x_min = 0
x_max = 10
y_min = 0
y_max = 8
H = 4
h = sqrt(68)

y1 = [[0, 0], [H, 8]]
y2 = [[H, 8], [10, 0]]

def line(x, y):
    return (x - y[0][0]) * (y[1][1] - y[0][1]) / (y[1][0] - y[0][0]) + y[0][1]


def is_inside_triangle(x, y):
    if y <= line(x, y1) and y <= line(x, y2) and y >= 0:
        return True
    else:
        return False


num_points = 1000
points_inside = 0


for i in range(num_points):
    x = random.uniform(x_min, x_max)
    y = random.uniform(y_min, y_max)
    if is_inside_triangle(x, y):
        plt.scatter(x, y, color = 'green')
        points_inside += 1
    else:
        plt.scatter(x, y, color = 'red')


area = (x_max - x_min) * (y_max - y_min) * points_inside / num_points


print("Площадь треугольника: ", x_max * h / 2)
print("Площадь треугольника, вычисленная методом Монте-Карло:", area)
print(f'{points_inside} точек из {num_points} внутри треугольника')

plt.plot([y1[0][0], y1[1][0]], [y1[0][1], y1[1][1]], color='black')
plt.plot([y2[0][0], y2[1][0]], [y2[0][1], y2[1][1]], color='black')
plt.xlim(0, 10)
plt.ylim(0, 8)
plt.show()
