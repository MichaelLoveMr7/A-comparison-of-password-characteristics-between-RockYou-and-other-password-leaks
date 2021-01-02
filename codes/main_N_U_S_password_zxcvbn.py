#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:37:04 2020

@author: yujiedong
"""
import os
os.getcwd()
os.chdir("/Users/yujiedong/Downloads/BreachCompilation/data")

from N_U_S_password import N_U_S_password_odd, N_U_S_password_even, N_U_S_ALL_password
import numpy as np
import pandas as pd
from CUS_0to9 import makeArrays
import matplotlib.pyplot as plt
from astropy.visualization import hist
from zxcvbn import zxcvbn
#/Users/yujiedong/Downloads/capstone papers/new password python file/main_BreachCompilation.py
pswd_data = pd.read_csv("/Users/yujiedong/Downloads/BreachCompilation/data/0", 
                        sep=":", header = None, error_bad_lines = False,
                        encoding="ISO-8859-1", engine = 'python')
#print(pswd_data.iloc[:2300000,1])
passwords = pswd_data.iloc[:,1]

passwords = passwords.to_frame()
passwords = passwords.astype(str)

count = 0
for count in passwords.index:
        count = count + 1
        
        
row = 0
zxcvbn_ALL = 0  
length_ALL = 0      
while row != count:
    password = passwords.iloc[row, 0]
    #get the zxcvbn score
    zxcvbn_results=zxcvbn(password)
    zxcvbn_score = zxcvbn_results.get('score')
    #print('zxcvbn_score',zxcvbn_score)
    zxcvbn_ALL = zxcvbn_ALL + zxcvbn_score            
    length = len(password) 
    length_ALL = length_ALL + length       
    row = row + 1    
    
zxcvbn_average = zxcvbn_ALL/count
count = ["customer_count:", count]
zxcvbn_ALL = ["zxcvbn_ALL:",zxcvbn_ALL]
zxcvbn_average = ["zxcvbn_average:",zxcvbn_average]
print(count, zxcvbn_ALL, zxcvbn_average)



        
        
