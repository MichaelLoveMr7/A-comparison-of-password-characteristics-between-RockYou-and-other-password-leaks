#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 15:50:33 2020

@author: yujiedong
"""

import os
os.getcwd()
os.chdir("/Users/yujiedong/Downloads/BreachCompilation/data")

from N_U_S_password import N_U_S_password_odd, N_U_S_password_even
from N_U_S_password import N_U_S_password_odd_even, N_U_S_ALL_password
import numpy as np
import pandas as pd
from CUS_0to9 import makeArrays
#import matplotlib.pyplot as plt
#from astropy.visualization import hist
#from zxcvbn import zxcvbn

pswd_data = pd.read_csv("/Users/yujiedong/Downloads/BreachCompilation/data/combined_m_half3_i.txt", 
                         header = None, error_bad_lines = False,
                        sep=":",encoding="ISO-8859-1", engine = 'python')

passwords = pswd_data.iloc[:,1]

passwords = passwords.to_frame() 
passwords = passwords.astype(str)
#print(passwords)
count = 0
for count in passwords.index:
        count = count + 1
        
N1ALL,  N3ALL = 0,  0
U1ALL,  U3ALL = 0,  0
S1ALL,  S3ALL = 0,  0



row = 0
count_odd_even = 0

length_ALL = 0


#zxcvbn_ALL = 0
while row != count:
    password = passwords.iloc[row, 0]
    
    length = len(password)
    N1, N3, U1, U3, S1, S3 = N_U_S_password_odd_even(password,length)
    
    N1ALL = N1ALL + N1
    #print("N1ALL:",N1ALL)
    N3ALL = N3ALL + N3
    U1ALL = U1ALL + U1
    U3ALL = U3ALL + U3
    S1ALL = S1ALL + S1
    #print("N1ALL:",S1ALL)
    S3ALL = S3ALL + S3
    count_odd_even = count_odd_even + 1
    

    row = row + 1
    
count_odd_even = ['count_odd_even:', count_odd_even ]
N1ALL = ['N1ALL:', N1ALL]
N3ALL = ['N3ALL:',  N3ALL]
U1ALL = ['U1ALL:', U1ALL]
U3ALL = ['U3ALL:',  U3ALL]
S1ALL = ['S1ALL:', S1ALL]
S3ALL = ['S3ALL:',  S3ALL]

np.savetxt('New_combined_m_half3_i.csv', (  count_odd_even,
                                     N1ALL, N3ALL, 
                                     U1ALL,U3ALL, 
                                     S1ALL, S3ALL                      
        ), fmt='%s')
result_data=pd.read_csv('New_combined_m_half3_i.csv',sep=":",header = None)
result_data.to_csv('New_combined_m_half3_i.csv')




