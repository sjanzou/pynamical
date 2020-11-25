import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0.,1.1,0.1)
plt.axis([0.,1.,0.,1.])
plt.plot(x,0.8*x*(1.-x),'r--',x,2.7*x*(1.-x),'g-.')
plt.ylabel('$x_{n+1}$')
plt.xlabel('$x_n$')

plt.show()