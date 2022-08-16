from one_center import *
import matplotlib.pyplot as plt
import random

n=10
p_max=1
x_min, x_max, y_min, y_max = -10, 10, -10, 10

for p in range(p_max):
    p_list = []
    for i in range(n):
        p_list.append(Vec2D(random.uniform(x_min, x_max), random.uniform(y_min, y_max)))
    circle1, r1 = smallest_enclosing_circle(p_list)

    
print(circle1, r1)
circle_plot1 = plt.Circle(circle1.coordinate(), r1, color='r', fill=False)
plt.gca().add_patch(circle_plot1)

for i in range(n):
    plt.scatter(p_list[i].x, p_list[i].y, color = 'black')

extra_width = 5
plt.xlim([x_min-extra_width, x_max+extra_width])
plt.ylim([y_min-extra_width, y_max+extra_width])
plt.gca().set_aspect('equal')
plt.show()