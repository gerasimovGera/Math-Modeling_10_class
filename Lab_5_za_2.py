import matplotlib.pyplot as plt
import numpy as np

def gip(k):
    x = np.arange(-10,10,1)
    y = k/x
    plt.plot(x,y)
    plt.show()
    

gip(6)





