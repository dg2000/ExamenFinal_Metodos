# Ejercicio5
# Resuelva el siguiente sistema acoplado de ecuaciones diferenciales 
# dx/dt = sigma * (y - x)
# dy/dt = rho * x - y -x*z
# dz/dt = -beta * z + x * y
# con sigma = 10, beta=2.67, rho=28.0,
# condiciones iniciales t=0, x=0.0, y=0.0, z=0.0, hasta t=5.0.
# Prepare dos graficas con la solucion: de x vs y (xy.png), x vs. z (xz.png) 

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import numpy as np


t = 0.0
x = 0.0
y = 0.0
z = 0.0

sigma = 10.0
beta = 2.67
rho = 28.0

ts = np.array([0.0])
xs = np.array([0.0])
ys = np.array([0.0])
zs = np.array([0.0])

h = 1.0/100.0

def dxdt(x, y, z):
    
    return sigma*(y-x)

def dydt(x, y, z):
        
    return rho * x - y - x*z

def dzdt(x, y, z):
    
    return -beta*z + x*y

def guarda(t, x, y, z):
    np.append(t, ts)
    np.append(x, xs)
    np.append(y, ys)
    np.append(z, zs)

while(t <= 5.0):

    t_old = t
    x_old = x
    y_old = y
    z_old = z
    
    t = t_old + h
    
    x = x_old + h*dxdt(x_old, y_old, z_old)
    
    y = y_old + h*dydt(x_old, y_old, z_old)
    
    z = z_old + h*dzdt(x_old, y_old, z_old)

    guarda(t, x, y, z)


plt.plot(ys, xs, label = "x vs y")
plt.savefig("xy.png")


plt.figure()
plt.plot(zs, xs, label = "x vs. z")
plt.savefig("xz.png")
    
    