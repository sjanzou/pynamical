import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0.,1.1,0.1)
plt.axis([0.,1.,0.,1.])
plt.plot(x,0.8*x*(1.-x),'r--',label='$x_{n+1}=0.8*x_n*(1-x_n)$')
plt.plot(x, 2.7*x*(1.-x),'g-.',label='$x_{n+1}=2.7*x_n*(1-x_n)$')
plt.plot(x, x,'b',label='$x_{n+1}=x_n$')
plt.ylabel('$x_{n+1}$')
plt.xlabel('$x_n$')
plt.legend(loc="upper left")
plt.show()