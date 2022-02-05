from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import random
import math


gridFile = input("Please enter the name of the file: ")
x = []
y = []
file = open(gridFile,"r")
Start = file.readline().strip().split()
x.append(int(Start[0]))
y.append(int(Start[1]))
Goal = file.readline().strip().split()
x.append(int(Goal[0]))
y.append(int(Goal[1]))
Size = file.readline()
vertices = file.readlines()
blocked_x = []
blocked_y = []
for vertz in vertices:
    to_be_blocked = vertz.strip().split()
    if int(to_be_blocked[2])==1:
        blocked_x.append(int(to_be_blocked[0]))
        blocked_x.append(int(to_be_blocked[0]))
        blocked_x.append(int(to_be_blocked[0])+1)
        blocked_x.append(int(to_be_blocked[0])+1)
        blocked_y.append(int(to_be_blocked[1]))
        blocked_y.append(int(to_be_blocked[1])+1)
        blocked_y.append(int(to_be_blocked[1]))
        blocked_y.append(int(to_be_blocked[1])+1)

plt.plot(x,y, 'o', color='orange', zorder=3)
plt.plot(blocked_x,blocked_y, 'o', color='blue', zorder=2)
plt.grid()
plt.show()
file.close()