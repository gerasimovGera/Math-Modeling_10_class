import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.arange(0,4,1)
def credit(n,t):
    dmdf=-k*n*t
    return dmdf
M_0=1000
bak_I=0.08
k=bak_I
solve_bk=odeint(credit,M_0,t)
plt.plot(t,solve_bk[:,0])
plt.show()