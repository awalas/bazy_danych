# Aneta Walas zad3 lab1- definicja oraz wykres funkcji x^2+5

import matplotlib.pyplot as plt
import numpy as np

def exercise3(x):
	return x**2+5

x1=np.linspace(-1,1,100)
y1=exercise3(x1)

x2=np.linspace(-6,6,100)
y2=exercise3(x2)

x3=np.linspace(0,5,100)
y3=exercise3(x3)

figure, axs = plt.subplots(3)

axs[0].set_title('x>-1 x<1')	
axs[0].plot(x1,y1)
axs[0].set_xlabel('x')
axs[0].set_ylabel('y')
axs[0].legend(['x^2+5'])

axs[1].set_title('x>-6 x<6')	
axs[1].plot(x2,y2)
axs[1].set_xlabel('x')
axs[1].set_ylabel('y')
axs[1].legend(['x^2+5'])

axs[2].plot(x3,y3)
axs[2].set_title('x>0 x<5')
axs[2].set_xlabel('x')
axs[2].set_ylabel('y')
axs[2].legend(['x^2+5'])
plt.show()
	
