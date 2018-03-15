# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:59:49 2018

by Shubham
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use("classic")

import numpy as np
x=np.linspace(0,10,100)
plt.plot(x,np.sin(x))
plt.plot(x,np.cos(x))
plt.show()
x

%matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use("classic")

import numpy as np
x=np.linspace(0,10,100)
plt.plot(x,np.sin(x))
plt.plot(x,np.cos(x))
plt.show()

fig=plt.figure()
fig.savefig("myfigure3.png")
!dir *.png



%matplotlib inline
plt.subplot(2,1,1)
plt.plot(x,np.sin(x),"--")

plt.subplot(2,1,2)
plt.plot(x,np.cos(x))



fig,ax=plt.subplots(3)
ax[0].plot(x,np.sin(x))
ax[1].plot(x,np.cos(x))
ax[2].plot(x,np.tan(x))



%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")
import numpy as np
fig=plt.figure()
ax=plt.axes()
x=np.linspace(0,10,1000)
ax.plot(x,np.sin(x))


plt.plot(x,np.sin(x-0),color="blue",linestyle="-")
plt.plot(x,np.sin(x-1),color="yellow",linestyle="-.")
plt.plot(x,np.sin(x-2),color="#FF00FF")
plt.plot(x,np.sin(x-3),color="g")