import numpy as np
from matplotlib import pyplot as plt
from algoart import distorted

ax = np.empty([0,1])
ay = np.empty([0,1])
r = 0

for i in np.linspace(0, 10, 10):
    for j in np.linspace(0, 10, 10):
        x,y = distorted.rectangle(-0.35, -0.35, 0.35, 0.35, steps=10, dist_level=0.07)

        nx = x * np.cos(r) - y * np.sin(r)  #here we rotate
        ny = x * np.sin(r) + y * np.cos(r)

        ax = np.append(ax, nx+j)
        ay = np.append(ay, ny+i)
        ax = np.append(ax, np.nan)
        ay = np.append(ay, np.nan)

        nx,ny = distorted.circle(0, 0, 0.125, steps=10, distort_level=0)
        ax = np.append(ax, nx+j)
        ay = np.append(ay, ny+i)
        ax = np.append(ax, np.nan)
        ay = np.append(ay, np.nan)


        r = r + np.pi/180*i*2

x,y = distorted.rectangle(-1, -1, 11, 11, steps=100, dist_level=0.07)
ax = np.append(ax, x)
ay = np.append(ay, y)
ax = np.append(ax, np.nan)
ay = np.append(ay, np.nan)

plt.plot(ax,ay)
plt.axis('off')
plt.axis('equal')
plt.savefig("random_rotating_squares.svg")
plt.show()

