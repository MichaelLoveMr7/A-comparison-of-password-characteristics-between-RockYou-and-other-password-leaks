#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:16:45 2020

@author: yujiedong
"""

import glob
import os
import pandas as pd
from scipy import stats


os.chdir("/Users/yujiedong/Downloads/BreachCompilation/data")

Ttest = pd.read_csv("T-testALL.csv")

length_1p4B = len(Ttest)
count = 0

array1 = []

while(count < 4):
    
    array1.append(Ttest.iloc[count, 2])
    
    count = count + 1
    print(array1)
    

count = 5
#i = 0
array2 = []
#array1.append(combined_csv.iloc[100, 2])
#print(array1)
while(count <  9):
    array2.append(Ttest.iloc[count, 2])
    
    count = count + 1
    print(array2)

print('array1',array1)
print('array2',array2)
print(stats.ttest_ind(array1, array2))