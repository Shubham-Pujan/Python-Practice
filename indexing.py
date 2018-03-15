# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:31:23 2018

by Shubham
"""
#%%fancy indexing


import array
import numpy as np
import pandas
a=np.arange(0,80,10)
a

 
y=a[[1,2,-3]]

z=[a[1],a[2],a[-3]]
z
type(z)
type(y)

print(y)
y

y1=np.take(a,[1,2,-3])
y1
type(y1)
l=[1,2,-3]
y2=np.take(a,l)
y2






# %% mask command

a=np.array([1,2,3,4,5])
mask=np.array([1,0,1,0,1],dtype=bool)
mask
y=a[mask]
y

y=np.compress(mask,a)
y
type(y)



# %% array calculatuon methods

a=np.array([[1,2,3],[4,5,6]],float)
a
a.sum()
np.sum(a)
np.sum(a,axis=0)
np.sum(a,axis=1)
sum(a)
%timeit a.sum()
%timeit np.sum(a)

np.amax(a)
np.amax(a,axis=0)
np.amax(a,axis=1)
a.max()





np.average(a,axis=0,weights=(1,2))


b=np.arange(1,5)
b


b=a.flatten()
b
a

a=np.arange(6)
a
a.resize(2,3)
a
id(a)
b=a.ravel()
b
id(b)
b
a

a.swapaxes(0,1)

x=np.array([1,2,3,4,5,6])
x
x.reshape(2,3)
x.reshape(3,2)
x12=x.reshape((2,3))
x12


x12.transpose()
numpy.squeeze(a)



x = np.array([[[0], [1], [2]]])
x
x.shape
(1, 3, 1)
np.squeeze(x)
np.squeeze(x).shape
