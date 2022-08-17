from p_center_func import *
import matplotlib.pyplot as plt
import random

n=10
p_max=3
x_min, x_max, y_min, y_max = -10, 10, -10, 10

points_list = []
for i in range(n):
    points_list.append(Vec2D(random.uniform(x_min, x_max), random.uniform(y_min, y_max)))

for p in range(p_max, p_max+1):
    groups = [[] for i in range(p)]
    #print(groups, len(groups))
    center_list = random.sample(points_list, p)
    #for center in center_list:
        #groups.append([center]) 
    for point in points_list:
        d_min, index = (x_max - x_min) * 10, 0
        for i in range(len(center_list)):
            d = distance(point, center_list[i])
            #print(point, center_list[i], d, d_min, i)
            if d < d_min:
                d_min = d
                index = i
        #print(index, point)
        groups[index].append(point)
        
    radius_list = [[] for i in range(p)]  
    for i in range(len(groups)):
        circle1, r1 = smallest_enclosing_circle(groups[i])
        center_list[i] = circle1
        radius_list[i] = r1

print("\n|||||||||||||||\n") 
for g in groups:             
    print("-------") 
    for p in g:
        print(p)      
    

for i in range(n):
    plt.scatter(points_list[i].x, points_list[i].y, color = 'black')
for i in range(len(center_list)):
    plt.scatter(center_list[i].x, center_list[i].y, color = 'red')
    circle_plot1 = plt.Circle(center_list[i].coordinate(), radius_list[i], color='r', fill=False)
    plt.gca().add_patch(circle_plot1)


extra_width = 5
plt.xlim([x_min-extra_width, x_max+extra_width])
plt.ylim([y_min-extra_width, y_max+extra_width])
plt.gca().set_aspect('equal')
plt.show()