#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:01:53 2020

@author: yujiedong
"""
'''
from scipy import stats
import numpy as np

np.random.seed(1234578)

rvs1  = stats.norm.rvs(loc=5, scale=10, size=5000)
print(rvs1)
print(type(rvs1),len(rvs1))

rvs2 = stats.norm.rvs(loc=5, scale=10, size=500)
'''

import glob
import os
import pandas as pd
from scipy import stats


os.chdir("/Users/yujiedong/Downloads/BreachCompilation/data/final results(1 to last2)/1")

extension = 'csv'


all_filenames = [i for i in glob.glob('*.{}'.format(extension))] # ?
# combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])

length_1 = len(combined_csv)
count = 0
#i = 0
array1 = []
#array1.append(combined_csv.iloc[100, 2])
#print(array1)
while(count < length_1):
    
    array1.append(combined_csv.iloc[count, 2])
    
    
    if combined_csv.iloc[count, 1] == "N_1_to_last2_ALL/length_ALL":
        array1.append(combined_csv.iloc[count, 2])
       # i = i + 1
        
    if combined_csv.iloc[count, 1] == "U_1_to_last2_ALL/length_ALL":
        array1.append(combined_csv.iloc[count, 2])
       # i = i + 1
        
    if combined_csv.iloc[count, 1] == "S_1_to_last2_ALL/length_ALL":
        array1.append(combined_csv.iloc[count, 2])
        #i = i + 1
        
    count = count + 1

'''
data1 = array1.to_csv
data1 = data1.iloc[:,0]
data1 = data1.reset_index(drop=True)
data1.to_csv("/Users/yujiedong/Downloads/BreachCompilation/data/final results/combined_13_billion_1new.csv",index=False, encoding='utf-8-sig')
'''


os.chdir("/Users/yujiedong/Downloads/BreachCompilation/data/final results(1 to last2)/2")

extension = 'csv'

all_filenames = [i for i in glob.glob('*.{}'.format(extension))] # ?
# combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
# export to csv

length_2 = len(combined_csv)
count = 0
#i = 0
array2 = []
#array1.append(combined_csv.iloc[100, 2])
#print(array1)
while(count < length_2):
    array2.append(combined_csv.iloc[count, 2])
    
    
    if combined_csv.iloc[count, 1] == "N_1_to_last2_ALL/length_ALL":
        array2.append(combined_csv.iloc[count, 2])
       # i = i + 1
        
    if combined_csv.iloc[count, 1] == "U_1_to_last2_ALL/length_ALL":
        array2.append(combined_csv.iloc[count, 2])
       # i = i + 1
        
    if combined_csv.iloc[count, 1] == "S_1_to_last2_ALL/length_ALL":
        array2.append(combined_csv.iloc[count, 2])
        #i = i + 1
        
    count = count + 1

print(stats.ttest_ind(array1, array2))

'''
#reopen combined_csv.csv

data = combined_csv.iloc[:,2]# Use percentage to avoid unbalanced data
data = data.reset_index(drop=True)
# export it to csv
data.to_csv("/Users/yujiedong/Downloads/BreachCompilation/data/final results/combined_13_billion_2new.csv",index=False, encoding='utf-8-sig')
'''
#print(rvs2)

#/Users/yujiedong/Downloads/BreachCompilation/data/final results/scores_combined_a_0to9.csv
'''
os.chdir("/Users/yujiedong/Downloads/BreachCompilation/data/final results")
rvs1 = pd.read_csv('combined_13_billion_1new.csv')
rvs1 = rvs1.iloc[:, 0]

rvs2 = pd.read_csv('combined_13_billion_2new.csv')
rvs2 = rvs2.iloc[:, 0]
print(stats.ttest_ind(rvs1, rvs2))
'''