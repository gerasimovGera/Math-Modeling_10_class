from math import cos,pi 
from constant_modulle import g
h = 100 
B = 30 
a = pi/3
v = ( (g*h*cos(B)**2)/(2*cos(a)**2*(1-cos(B)*cos(a))) )**0.5
print(v)


from constant_modulle import k,eil,h 
T=200
e=300

N = 2/pi**0.5 *  h/(k*T)**(3/2) * eil**(-e/k*T) * e**(T/2)
print(N)