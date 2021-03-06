import numpy
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.gca(projection='3d')

t = np.arange(0.01,4*np.pi,0.01)
R = 1

x = 2**(-0.1*t)*np.cos(t)
y = 2**(-0.1*t)*np.sin(t)
z = -t


ax.plot(x,y,z,label='Dich')
ax.legend()

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('3D Test')

