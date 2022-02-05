from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import random
import math



##Creating the grid and Choosing two points 
x_length = int(input("Please enter a size for the x-axis: "))
y_length = int(input("Please enter a size for the y-axis: "))

blocked_vertz = math.floor(((x_length+1)*(y_length+1))*0.1)
rand_y = []
rand_x = []
for i in range(0,2):
    rand_x.append(random.randint(1,x_length))
for j in range(0,2):
    rand_y.append(random.randint(1,y_length))

x=0
blocked_count = 0
myFile = open("test.txt","w")
myFile.write(str(rand_x[0])+" "+str(rand_x[1]))
myFile.write("\n")
myFile.write(str(rand_y[0])+" "+str(rand_y[1]))
myFile.write("\n")
myFile.write(str(x_length)+" "+str(y_length)+"\n")
for i in range(1,x_length+1):
    for j in range(1,y_length+1):
        r = random.randint(0,1)
        if r==1:
            if blocked_count != blocked_vertz:
                blocked_count+=1
                x=1
        else:
            x=0
        myFile.write(str(i)+" "+str(j)+" "+str(x)+"\n")
myFile.close()


x = []
y = []
file = open("test.txt","r")
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