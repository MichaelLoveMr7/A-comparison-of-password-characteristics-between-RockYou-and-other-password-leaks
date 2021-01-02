#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 16:01:12 2020

@author: yujiedong
"""

import os
import pandas as pd
from scipy import stats
from N_U_S_password import N_U_S_password_0toLast, zxcvbn_array
import re



os.chdir("/Users/yujiedong/Downloads/BreachCompilation/data")

pswd_data = pd.read_csv("combined_Random.txt", 
                         header = None, sep = ":",
                         error_bad_lines = False,
                         encoding='ISO-8859-1')

#pswd_data1 = pswd_data.iloc[:,1]
N_array1 = []

U_array1 = []

S_array1 = []
N_U_array1 = []
U_S_array1 = []
N_S_array1 = []
N_U_S_array1 = []

length_dataset = len(pswd_data)

count = 0
count_N = 0
count_S = 0
count_U = 0
count_N_U = 0
count_U_S = 0
count_N_S = 0
count_N_U_S = 0

while(count != length_dataset ):
   N_0_to_last = 0
   U_0_to_last = 0
   S_0_to_last = 0
   password = pswd_data.iloc[count,1]
   #print(password)
   
   length_pass = len(str(password))
   if length_pass < 20:
       N_0_to_last, U_0_to_last, S_0_to_last = N_U_S_password_0toLast(password, length_pass)
       while( N_0_to_last > 0 and count_N != 3000):
           N_array1.append(password)
           #print(N_array1)
           count_N = count_N + 1
           break
           
       while( U_0_to_last > 0 and count_U != 3000) :   
           U_array1.append(password)
           count_U = count_U + 1
           break
       
       while(S_0_to_last > 0 and count_S != 3000):    
           S_array1.append(password)
           count_S = count_S + 1
           break
           
       while( N_0_to_last > 0 and U_0_to_last > 0 and count_N_U != 3000):
           N_U_array1.append(password)
           count_N_U = count_N_U + 1
           break
           
       while( U_0_to_last > 0 and S_0_to_last > 0 and count_U_S != 3000):
           U_S_array1.append(password)
           count_U_S = count_U_S + 1
           break
       while( N_0_to_last > 0 and S_0_to_last > 0 and count_N_S != 3000):
           N_S_array1.append(password)
           count_N_S = count_N_S + 1
           break
       while( N_0_to_last > 0 and S_0_to_last > 0 and U_0_to_last > 0 and count_N_U_S != 3000):
           N_U_S_array1.append(password)
           count_N_U_S = count_N_U_S + 1
           print(count_N_U_S)
           print(count)
           break
   
   count = count + 1    
   #print("count",count) 
   '''
N_array1_df = pd.DataFrame(N_array1)
U_array1_df = pd.DataFrame(U_array1)
S_array1_df = pd.DataFrame(S_array1)
N_U_array1_df = pd.DataFrame(N_U_array1)
U_S_array1_df = pd.DataFrame(U_S_array1)
N_S_array1_df = pd.DataFrame(N_S_array1)
N_U_S_array1_df = pd.DataFrame(N_U_S_array1)
Billion_array_3000 = pd.concat([N_array1_df, U_array1_df,S_array1_df,
                                N_U_array1_df, U_S_array1_df,
                           N_S_array1_df, N_U_S_array1_df], axis =1)
Billion_array_3000.to_csv('Billion_array_3000.csv',
                          header = ["N_array1", "U_array1",
                          "S_array1", "N_U_array1", "U_S_array1",
                           "N_S_array1", "N_U_S_array1"],index = True)
   ''' 
U_array1_zxcvbn, len_passwords1 = zxcvbn_array(U_array1)
N_array1_zxcvbn, len_passwords2 = zxcvbn_array(N_array1)
S_array1_zxcvbn, len_passwords3 = zxcvbn_array(S_array1)
N_U_array1_zxcvbn, len_passwords4 = zxcvbn_array(N_U_array1)
U_S_array1_zxcvbn, len_passwords5 = zxcvbn_array(U_S_array1)
N_S_array1_zxcvbn, len_passwords6 = zxcvbn_array(N_S_array1)
N_U_S_array1_zxcvbn, len_passwords7 = zxcvbn_array(N_U_S_array1)

print("length_dataset:",length_dataset)
print("password_count:", count)
print("U_array1_zxcvbn, len_passwords:",U_array1_zxcvbn, ",",len_passwords1)
print("N_array1_zxcvbn, len_passwords:", N_array1_zxcvbn, ",",len_passwords2)
print("S_array1_zxcvbn, len_passwords:", S_array1_zxcvbn, ",",len_passwords3)   
print("N_U_array1_zxcvbn, len_passwords:", N_U_array1_zxcvbn,",", len_passwords4)  
print("U_S_array1_zxcvbn, len_passwords:", U_S_array1_zxcvbn, ",",len_passwords5)
print("N_S_array1_zxcvbn, len_passwords:", N_S_array1_zxcvbn, ",",len_passwords6)
print("N_U_S_array1_zxcvbn, len_passwords:", N_U_S_array1_zxcvbn, ",",len_passwords7)



















