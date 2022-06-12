import numpy as np
import matplotlib.pyplot as plt

startPoint = -1.139
endPoint = 1.139
interval = 0.0001

xS, yUppers, yLowers = [], [], [], 
x = startPoint
while x <= endPoint:
    xS.append(x)

    yUpper = 0.5*(pow(abs(x), (2/3)) + pow((pow(abs(x), (4/3)) + 4 * (1 - pow(abs(x), 2))), 0.5))
    yUppers.append(yUpper)

    yLower = 0.5*(pow(abs(x), (2/3)) - pow((pow(abs(x), (4/3)) + 4 * (1 - pow(abs(x), 2))), 0.5))
    yLowers.append(yLower)
    x += interval

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot((-3, 0, 0, 0, 3, 0, 0, 0), (0, 0, 2, 0, 0, 0, -2, 0), color='black', linewidth = 1)
ax.plot(xS, yUppers)
ax.plot(xS, yLowers)
plt.show()