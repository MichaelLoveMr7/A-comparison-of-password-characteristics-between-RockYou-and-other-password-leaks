#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 13:21:04 2020

@author: yujiedong
"""




import glob
import os
import pandas as pd
from scipy import stats


os.chdir("/Users/yujiedong/Downloads/BreachCompilation/data/final results(1 to last2)")

data_1p4B = pd.read_csv('combined_13B_1TOlast2.csv')


length_1p4B = len(data_1p4B)
count = 5

array1 = []

while(count < length_1p4B):
    
    array1.append(data_1p4B.iloc[count, 2])
    
    count = count + 1
    
    
data_rockyou = pd.read_csv('Rockyou_pass[1]_to_pass[length-2].csv')
length_2 = len(data_rockyou)
count = 5
#i = 0
array2 = []
#array1.append(combined_csv.iloc[100, 2])
#print(array1)
while(count < length_2):
    array2.append(data_rockyou.iloc[count, 2])
    
    count = count + 1

print('array1',array1)
print('array2',array2)
print(stats.ttest_ind(array1, array2))
    