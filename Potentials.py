

#imports

import astropy.constants as c
import astropy.units as u
import numpy as np
from numpy import linspace
import mpmath
import math
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt



e0= c.eps0.value
r=.01
q=1



phi= (1/(4*np.pi*e0)*(q/r))



#Creating the arrays



N = 30
POT = np.zeros([N, N])
x=np.linspace(0, 1, num=N)
y=x
xp=np.array([.45,.55])#coordinate of point

yp=np.array([.50,.50])#coordinate of point
    
for i in range (N):#one for rows
    
    for j in range (N):#one for col
        x_local=x[j]
        y_local=y[i]
        r1=np.sqrt((x[j]-xp[0])**2+(y[i]-yp[0])**2)
        r2=np.sqrt((x[j]-xp[1])**2+(y[i]-yp[1])**2)
        POT[i][j]=(1/(4*np.pi*e0)*(q/r1))+(1/(4*np.pi*e0)*(-q/r2))



#plotting Electric Potentials
x1 = np.linspace(-5, 5, 30)
y1 = np.linspace(-5, 5, 30)

X1, Y1 = np.meshgrid(x1, y1)
Z1 = POT

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(X1, Y1, Z1, rstride=1, cstride=3,
                cmap='cool', edgecolor='black')
ax.set_title('Electric potentials')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');



#take derivative of both x and y, using a central difference formula f(x+h)-f(x-h)/2h saving them in arrays. 
#This gives you an electric field

h= 1/N

Ex= np.zeros([N, N])
Ey= np.zeros([N, N])


for i in range (1,N-1):
    
    for j in range (1,N-1):
        
        dx=(POT[i+1][j]-POT[i-1][j])/(2*h)
        dy=(POT[i][j+1]-POT[i][j-1])/(2*h)
        Ex[i][j]=dx
        Ey[i][j]=dy




scale=1e-15


fig, ax = plt.subplots()
for i in range (1,30,2):
    for j in range (1,30,2):
        plt.arrow(x[j], y[i], scale*Ex[i][j], scale*Ey[i][j], color='blue')
ax.set_title('electric field')
ax.set_ylim()

plt.show()





