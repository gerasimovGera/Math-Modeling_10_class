import numpy as np 
from scipy.integrate import odeint 
import matplotlib.pyplot as plt

t=np.arange(0,50,0.01)
def diff(z,t):
    y,w=z
    dy_dt=w
    dw_dt=-np.sin(y)-k/m*w
    return dy_dt,dw_dt


y_0 = 30
w_0 = 0.5
z0 = y_0,w_0

k = 1
m = 10

sol=odeint(diff,z0,t)
plt.plot(t,sol[:,0])
plt.legend()
plt.show()
    