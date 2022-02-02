from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import random


##Creating the grid and Choosing two points 
x_length = int(input("Please enter a size for the x-axis: "))
y_length = int(input("Please enter a size for the y-axis: "))

vertices_used = []
#x_length = 10
#y_length = 10
rand_y = []
rand_x = []
for i in range(0,2):
    rand_x.append(random.randint(1,x_length))
vertices_used = rand_x + vertices_used
for j in range(0,2):
    rand_y.append(random.randint(1,y_length))

##Creating the blocked boxes
blocked_x = []
blocked_y = []
for i in range(x_length):
    n = random.randint(1,x_length)
    blocked_x.append(n)
    blocked_x.append(n)
    blocked_x.append(n+1)
    blocked_x.append(n+1)
for i in range(y_length):
    n = random.randint(1,y_length)
    blocked_y.append(n)
    blocked_y.append(n+1)
    blocked_y.append(n)
    blocked_y.append(n+1)


plt.plot(blocked_x,blocked_y, 'o', color='blue')

plt.plot(rand_x,rand_y, 'o', color='orange')
plt.grid(True)
plt.show()