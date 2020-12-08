# "" A simple ODE solver to describe the Lorenz Attractor Phenomenon  "" 
# Detailed explaination https://www.stsci.edu/~lbradley/seminar/attractors.html

#importing necessary libraries 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# x, y, z: any point of space on 3D space
# p is the Prandtl number representing the ratio of the fluid viscosity to its thermal conductivity
 #r is the difference in temperature between the top and bottom of the system
 #b is the ratio of the width to height of the box used to hold the system (8/3)
def lorenz(x, y, z, p=10, r=28, b=2.667):
	x_dot = p*(y - x)
	y_dot = r*x - y - x*z
	z_dot = x*y - b*z
	return x_dot, y_dot, z_dot
dt = 0.01
num_steps =10000 #10....10^2,10^3,10^4,10^5....

# Initializing the values
xp = np.empty(num_steps + 1)
yp = np.empty(num_steps + 1)
zp = np.empty(num_steps + 1)

# setting the initial values for the computation
xp[0], yp[0], zp[0] = (0., 1., 1.05)

# Getting to "time" and computing the partial derivatives at the current point and than utilizing it to estimate the next point

for i in range(num_steps):
    x_dot, y_dot, z_dot = lorenz(xp[i], yp[i], zp[i])
    xp[i + 1] = xp[i] + (x_dot * dt)
    yp[i + 1] = yp[i] + (y_dot * dt)
    zp[i + 1] = zp[i] + (z_dot * dt)
# Saving the results, it can be saved at each time stop or at every discrete point
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(xp, yp, zp, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")
plt.show()

