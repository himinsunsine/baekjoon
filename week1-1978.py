# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 14:10:31 2023

@author: himinsunsine
"""

n = int(input())

arr = list(map(int, input().split(' ')))

num = 0

for i in arr:
    cnt =0
    if(i==1):
        continue
    for j in range(2,i+1):
        if(i%j ==0):
            cnt+=1
    if(cnt==1):
        num +=1
        
print(num)
        
