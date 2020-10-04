#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 18:17:37 2020

@author: yujiedong
"""

from N_U_S_password import N_U_S_password_odd, N_U_S_password_even, N_U_S_ALL_password
import numpy as np
import pandas as pd
from CUS_0to9 import makeArrays
import matplotlib.pyplot as plt
#from astropy.visualization import hist

import os
os.getcwd()
os.chdir("/Users/yujiedong/Downloads/BreachCompilation/data")
#/Users/yujiedong/Downloads/capstone papers/new password python file/main_BreachCompilation.py
pswd_data = pd.read_csv("/Users/yujiedong/Downloads/BreachCompilation/data/rockyou.txt", 
                         header = None, error_bad_lines = False,
                        encoding="ISO-8859-1", engine = 'python')
#print(pswd_data.iloc[:2300000,1])
passwords = pswd_data.iloc[:,0]

passwords = passwords.to_frame()
passwords = passwords.astype(str)
#print(passwords)
count = 0
for count in passwords.index:
        count = count + 1
        
row = 0
#count_odd = 0
#count_even = 0
N_1_to_last2_ALL = 0
U_1_to_last2_ALL = 0
S_1_to_last2_ALL = 0
length_password_ALL_SUM = 0
while row != count:
    password = passwords.iloc[row, 0]
    length = len(password)
    N_1_to_last2, U_1_to_last2, S_1_to_last2 = N_U_S_ALL_password(password, length)
    N_1_to_last2_ALL = N_1_to_last2_ALL + N_1_to_last2
    U_1_to_last2_ALL = U_1_to_last2_ALL + U_1_to_last2
    S_1_to_last2_ALL = S_1_to_last2_ALL + S_1_to_last2
    length_password_ALL_SUM = length_password_ALL_SUM + length
    row = row + 1
    
print("N_1_to_last2_ALL:", N_1_to_last2_ALL)
print("U_1_to_last2_ALL:", U_1_to_last2_ALL)
print("S_1_to_last2_ALL:", S_1_to_last2_ALL)
print("count_odd_even:", row)
print("length_password_ALL_SUM:",length_password_ALL_SUM)

count_odd_even = ["User_count_SUM:", row]
N_1_to_last2_ALL = ["N_1_to_last2_ALL_SUM:", N_1_to_last2_ALL]
U_1_to_last2_ALL = ["U_1_to_last2_ALL_SUM:", U_1_to_last2_ALL]
S_1_to_last2_ALL = ["S_1_to_last2_ALL_SUM:", S_1_to_last2_ALL]
length_password_ALL_SUM = ["length_password_ALL_SUM:",length_password_ALL_SUM]


np.savetxt('scores_Rockyou_1tolast2.csv', (  
                            count_odd_even,
                            N_1_to_last2_ALL,
                            U_1_to_last2_ALL,
                            S_1_to_last2_ALL,
                            length_password_ALL_SUM
                            ), fmt='%s')
result_data=pd.read_csv('scores_Rockyou_1tolast2.csv',sep=":",header = None)
result_data.to_csv('scores_Rockyou_1tolast2.csv')










    
    
    
    