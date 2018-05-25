# Ejercicio1
# A partir de los arrays x y fx calcule la segunda derivada de fx con respecto a x. 
# Esto lo debe hacer sin usar ciclos 'for' ni 'while'.
# Guarde esta segunda derivada en funcion de x en una grafica llamada 'segunda.png'
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2.,10)
fx = np.array([0., 0.0494, 0.1975, 0.4444, 0.7901,1.2346 , 1.7778, 2.4198, 3.1605, 4.])

primera = np.zeros(len(fx) - 1)

primera[0] = fx[1] - fx[0]
primera[1] = fx[2] - fx[1]
primera[2] = fx[3] - fx[2]
primera[3] = fx[4] - fx[3]
primera[4] = fx[5] - fx[4]
primera[5] = fx[6] - fx[5]
primera[6] = fx[7] - fx[6]
primera[7] = fx[8] - fx[7]
primera[8] = fx[9] - fx[8]


segunda = np.zeros(len(primera) - 1)

segunda[0] = primera[1] - primera[0]
segunda[1] = primera[2] - primera[1]
segunda[2] = primera[3] - primera[2]
segunda[3] = primera[4] - primera[3]
segunda[4] = primera[5] - primera[4]
segunda[5] = primera[6] - primera[5]
segunda[6] = primera[7] - primera[6]
segunda[7] = primera[8] - primera[7]


plt.plot(x[1:len(x)-1], segunda)
plt.savefig("segunda.png")





