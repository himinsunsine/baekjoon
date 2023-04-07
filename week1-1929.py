# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 13:46:09 2023

@author: himinsunsine
"""

n, m = map(int, input().split())

list = [True]*(m+1)
list[0] = False
list[1] = False

for i in range(2, int(m**0.5)+1):
    if list[i] :
        for j in range(i*2,m+1,i):
            list[j] = False
            
for i in range(n, m+1):
    if list[i]:
        print(i)
        
#에라토스테네스의 