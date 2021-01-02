#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 10:05:30 2020

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
pswd_com1 = pswd_data.iloc[0:1000000]
pswd_com1 = pd.DataFrame(pswd_com1)
pswd_com2 = pswd_data.iloc[5000000:6000000]
pswd_com2 = pd.DataFrame(pswd_com2)
pswd_com3 = pswd_data.iloc[10000000:11000000]
pswd_com3 = pd.DataFrame(pswd_com3)
frames = [pswd_com1, pswd_com2, pswd_com3]
result = pd.concat(frames)
pswd_data2 = result
print(pswd_data2.iloc[0,0])
#print(len(pswd_data2.iloc[29,0]))

length_dataset = len(pswd_data2)

pswd_data_array = []
count = 0

while(count != length_dataset):
    pswd_data_array.append(pswd_data2.iloc[count,0])
    count = count + 1
    print(count)
    
zxcvbn_pswd = 0
passwords_length = 0

zxcvbn_pswd, passwords_length = zxcvbn_array(pswd_data_array)
print('zxcvbn_pswd, passwords_length:',zxcvbn_pswd, passwords_length)

