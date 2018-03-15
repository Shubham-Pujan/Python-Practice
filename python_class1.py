# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 10:45:36 2018

by Shubham
"""

print('shubham\'s')

age =23
print("hello" + str(age))

a= ["a","b","c","d"]
a[0]
a[0]="sdsd"
a
a.pop()
a
b=a[0:2]
b
a=[1,4,8,5]
sorted(a)

import random
num = random.sample(range(1, 101), 100)
num
num1=sorted(num)
num1[0]           # minimum
num1[-1]        # maximum

num1[1]         # second minimum
num1[-2]
average = sum(num)/len(num) # average
average

# mid
length = len(num)
print(length)
if ((length % 2 )== 0):
      mid = (num1[(length//2)-1] + num1[(length//2)]) / 2
else:
      mid = (num1[(length//2)-1])

mid


#minimum

mini = num [0]
mini
for number in num :
    if number < mini :
        mini =number
print(mini)

# second minimum
mini2 = num [0]
for number in num :
    if ((number < mini2) and number > mini):
        mini2 =number
mini2

# maximum

maxi = num [0]
for number in num :
    if number > maxi :
        maxi =number
print(maxi)


# second maximum
maxi2 = num [0]
for number in num :
    if ((number > maxi2) and (number < maxi)):
        maxi2 =number
maxi2
