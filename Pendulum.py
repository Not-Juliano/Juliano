import numpy as np
import math
from math import sin
import matplotlib.pyplot as plt
a=0.0
b=100.0

h = 1e-2

timepoints=np.arange(a,b,h)

g= 9.8
l= 0.1
x = [179,0]
r = np.array(x)
#r=np.arange(179,0, -1)
rpoints=[]



def f(r,t):
    theta=r[0]
    omega=r[1]
    ftheta = omega
    fomega = -(g/l)*(sin((theta)))
    return np.array([ftheta,fomega],float) 


#RungaKutta
for t in timepoints:
    rpoints.append(r[0])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r= r+ (k1+2*k2+2*k3+k4)/6

plt.plot(timepoints,rpoints,'red')

import matplotlib.animation as animation



fig = plt.figure(figsize=(5,5))
ax = plt.axes(xlim=(-1, 1), ylim=(-1, 1))
pendulum = plt.Circle((.1, .1), radius=0.02, fc='r')

def init():
    pendulum.center = (0.1, 0.1)
    ax.add_patch(pendulum)
    return pendulum,

def animate(i):
    x = l*np.cos(rpoints[i]- (np.pi/2))
    y = l*np.sin(rpoints[i]-(np.pi/2))
    pendulum.center = (x, y)
    return pendulum,

anim = animation.FuncAnimation(fig, animate,
init_func=init,frames=360,interval=20,blit=True)
anim.save('Julianospendulum.mp4')
plt.show()