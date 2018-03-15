# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 14:56:09 2018

by Shubham
"""

import matplotlib.pyplot as plt
x=[1,2,3]
y=[2,4,1]
plt.plot(x,y)
plt.xlabel("x axis")
plt.ylabel("y axis")

x1=[1,2,3]
y1=[2,4,6]
x2=[5,8,9]
y2=[4,6,0]
plt.plot(x1,y1,label="line 1")
plt.plot(x2,y2,label="line 2")
plt.show()

plt.bar(x1,y1,tick_label=["one","two","three"])

import numpy as np
np.set_printoptions(threshold=np.inf)

marks=np.random.uniform(30,100,1000)
marks

import numpy as np1

np.all(marks>=30)
np1.all(marks<=100)
range=(20,100)
bins=10
plt.hist(marks,bins,range,color="pink",edgecolor="green",alpha=1)
