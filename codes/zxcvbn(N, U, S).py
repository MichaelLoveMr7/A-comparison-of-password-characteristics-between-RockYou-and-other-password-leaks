#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 17:52:07 2020

@author: yujiedong
"""

import os
import pandas as pd
from scipy import stats
from N_U_S_password import N_U_S_password_0toLast, zxcvbn_array
import re

os.chdir("/Users/yujiedong/Downloads/BreachCompilation/data")

pswd_data = pd.read_csv("rockyou.txt", 
                         header = None, 
                         error_bad_lines = False,
                         encoding='ISO-8859-1')
pswd_com1 = pswd_data.iloc[0:1000]
pswd_com1 = pd.DataFrame(pswd_com1)
pswd_com2 = pswd_data.iloc[5000000:5001000]
pswd_com2 = pd.DataFrame(pswd_com2)
pswd_com3 = pswd_data.iloc[10000000:10001000]
pswd_com3 = pd.DataFrame(pswd_com3)
frames = [pswd_com1, pswd_com2, pswd_com3]
result = pd.concat(frames)
pswd_data2 = result

#pswd_data2 = pswd_data.iloc[:,1]
#pswd_data2 = pd.DataFrame(pswd_data2)
N_array1 = []

U_array1 = []

S_array1 = []
N_U_array1 = []
U_S_array1 = []
N_S_array1 = []
N_U_S_array1 = []

length_dataset = len(pswd_data2)


count1 = 0


while(count1 != length_dataset ):
   N_0_to_last = 0
   U_0_to_last = 0
   S_0_to_last = 0
   password = pswd_data2.iloc[count1, 0]
   length_pass = len(str(password))
   N_0_to_last, U_0_to_last, S_0_to_last = N_U_S_password_0toLast(password, length_pass)
   if N_0_to_last > 0:
       N_array1.append(password)
       
   if U_0_to_last > 0:
       U_array1.append(password)
       
   if S_0_to_last > 0:
       S_array1.append(password)
       
   if N_0_to_last > 0 and U_0_to_last > 0:
       N_U_array1.append(password)
       
   if U_0_to_last > 0 and S_0_to_last > 0:
       U_S_array1.append(password)
       
   if N_0_to_last > 0 and S_0_to_last > 0:
       N_S_array1.append(password)
       
   if N_0_to_last > 0 and U_0_to_last > 0 and S_0_to_last > 0:
       N_U_S_array1.append(password)
       
   count1 = count1 + 1        
    
    
U_array1_zxcvbn, len_passwords1 = zxcvbn_array(U_array1)
N_array1_zxcvbn, len_passwords2 = zxcvbn_array(N_array1)
S_array1_zxcvbn, len_passwords3 = zxcvbn_array(S_array1)
N_U_array1_zxcvbn, len_passwords4 = zxcvbn_array(N_U_array1)
U_S_array1_zxcvbn, len_passwords5 = zxcvbn_array(U_S_array1)
N_S_array1_zxcvbn, len_passwords6 = zxcvbn_array(N_S_array1)
N_U_S_array1_zxcvbn, len_passwords7 = zxcvbn_array(N_U_S_array1)

print("length_dataset:", length_dataset)
print("U_array1_zxcvbn, len_passwords:",U_array1_zxcvbn, ",",len_passwords1)
print("N_array1_zxcvbn, len_passwords:", N_array1_zxcvbn, ",",len_passwords2)
print("S_array1_zxcvbn, len_passwords:", S_array1_zxcvbn, ",",len_passwords3)   
print("N_U_array1_zxcvbn, len_passwords:", N_U_array1_zxcvbn,",", len_passwords4)  
print("U_S_array1_zxcvbn, len_passwords:", U_S_array1_zxcvbn, ",",len_passwords5)
print("N_S_array1_zxcvbn, len_passwords:", N_S_array1_zxcvbn, ",",len_passwords6)
print("N_U_S_array1_zxcvbn, len_passwords:", N_U_S_array1_zxcvbn, ",",len_passwords7)   
        
        
        
        
        
        
        
        
        
        
    