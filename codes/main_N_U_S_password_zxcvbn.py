#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:37:04 2020

@author: yujiedong
"""
### spyder version 3.3.6
import os
os.getcwd()
os.chdir("/Users/yujiedong/Downloads/BreachCompilation/data")

from N_U_S_password import N_U_S_password_odd, N_U_S_password_even, N_U_S_ALL_password
import numpy as np
import pandas as pd
from CUS_0to9 import makeArrays
#import matplotlib.pyplot as plt
#from astropy.visualization import hist
from zxcvbn import zxcvbn



#/Users/yujiedong/Downloads/capstone papers/new password python file/main_BreachCompilation.py
pswd_data = pd.read_csv("/Users/yujiedong/Downloads/BreachCompilation/data/combined_random_zxcvbn.txt", 
                        sep = ":", header = None, error_bad_lines = False,
                        encoding="ISO-8859-1", engine = 'python')
#print(pswd_data.iloc[:2300000,1])
passwords = pswd_data.iloc[0:1000,1]
print("done")
passwords = passwords.to_frame()
passwords = passwords.astype(str)
'''
count = 0
for count in passwords.index:
        count = count + 1
'''
count = 1000       
        
row = 0
zxcvbn_ALL1 = 0  
length_ALL = 0      
while row < count:

    password = passwords.iloc[row, 0]
    #get the zxcvbn score
    zxcvbn_results=zxcvbn(password)
    zxcvbn_score = zxcvbn_results.get('score')
    print(zxcvbn_score,row)
    #print('zxcvbn_score',zxcvbn_score)
    zxcvbn_ALL1 = zxcvbn_ALL1 + zxcvbn_score            

    print(row,count)
    row = row + 1    
         
zxcvbn_average1 = zxcvbn_ALL1/1000
count1= ["Rockyou part1 customer_count:", count]
zxcvbn_ALL1 = ["Rockyou part1 zxcvbn_ALL:",zxcvbn_ALL1]
#zxcvbn_average1 = ["Rockyou part1 zxcvbn_average:",zxcvbn_average]
print(count1, zxcvbn_ALL1, zxcvbn_average1)


passwords = pswd_data.iloc[5000000:5001000,1]

passwords = passwords.to_frame()
passwords = passwords.astype(str)

print(passwords)
        
count = 1000       
row = 0
zxcvbn_ALL2 = 0  
 
while row < count:

    password = passwords.iloc[row, 0]
    #get the zxcvbn score
    zxcvbn_results=zxcvbn(password)
    zxcvbn_score = zxcvbn_results.get('score')
    print(zxcvbn_score,row)
    #print('zxcvbn_score',zxcvbn_score)
    zxcvbn_ALL2 = zxcvbn_ALL2 + zxcvbn_score            
 
    print(row,count)
    row = row + 1    
    
zxcvbn_average2 = zxcvbn_ALL2/1000
count2 = ["Rockyou part2 customer_count:", count]
zxcvbn_ALL2 = ["Rockyou part2 zxcvbn_ALL:",zxcvbn_ALL2]
#zxcvbn_average2 = ["Rockyou part2 zxcvbn_average:",zxcvbn_average]
print(count2, zxcvbn_ALL2, zxcvbn_average2)
        
        
passwords = pswd_data.iloc[10000000:10001000,1]

passwords = passwords.to_frame()
passwords = passwords.astype(str)

row = 0
count = 1000

zxcvbn_ALL3 = 0  
     
while row < count:

    password = passwords.iloc[row, 0]
    #get the zxcvbn score
    zxcvbn_results=zxcvbn(password)
    zxcvbn_score = zxcvbn_results.get('score')
    print(zxcvbn_score,row)
    #print('zxcvbn_score',zxcvbn_score)
    zxcvbn_ALL3 = zxcvbn_ALL3 + zxcvbn_score            
          
    row = row + 1    
    
 
zxcvbn_average3 = zxcvbn_ALL3/count

zxcvbn_average_ALL=(zxcvbn_average1 + zxcvbn_average2 + zxcvbn_average3)/3   
count3 = ["Rockyou part3 customer_count:", count]
zxcvbn_ALL3 = ["Rockyou part3 zxcvbn_ALL:",zxcvbn_ALL3]
#zxcvbn_average3 = ["Rockyou part3 zxcvbn_average:",zxcvbn_average]
print(count3, zxcvbn_ALL3, zxcvbn_average3)

zxcvbn_average_ALL=["zxcvbn_average_ALL:",zxcvbn_average_ALL]
zxcvbn_average1 = ["Rockyou part1 zxcvbn_average1:",zxcvbn_average1]
zxcvbn_average2 = ["Rockyou part2 zxcvbn_average2:",zxcvbn_average2]
zxcvbn_average3 = ["Rockyou part3 zxcvbn_average3:",zxcvbn_average3]

import numpy as np
np.savetxt('combined_random_zxcvbn.csv', (  
                            count1,zxcvbn_ALL1,zxcvbn_average1,
                            count2,zxcvbn_ALL2,zxcvbn_average2, 
                            count3,zxcvbn_ALL3,zxcvbn_average3,
                            zxcvbn_average_ALL
                                  ), fmt='%s')
result_data=pd.read_csv('combined_random_zxcvbn.csv',sep=":",header = None)
result_data.to_csv('combined_random_zxcvbn.csv')