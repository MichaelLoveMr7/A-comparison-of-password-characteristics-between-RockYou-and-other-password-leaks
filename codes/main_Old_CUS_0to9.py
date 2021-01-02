#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 17:41:09 2019

@author: yujiedong
"""

#password strength
import sys, math, re
from CUS_0to9 import check_password_length, check_password_uppercase
from CUS_0to9 import check_password_numbers, check_common_passwords
from CUS_0to9 import password_eval, makeArrays
import numpy as np
import pandas as pd
import random
import re

from numpy import genfromtxt
import unicodedata
import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from astropy.visualization import hist

#os.listdir()
#os.chdir(r'/Users/yujiedong/Downloads/password')
#with open("y", 'rb') as fopen:
#    q = fopen.read()
    #print(q.decode('latin-1'))

'''
for i,c in enumerate("rockyou.txt"):
    print(i, '%04x'% ord(c), unicodedata.category(c), end = " ")
    print(unicodedata.name(c))
'''
'''
f = open("rockyou.txt","r")
if f.mode =='r':
    contents = f.read()
    print(contents)
'''

#count = file_len(q.decode('latin-1'))

pswd_data = pd.read_csv("y", sep=":", header = None, error_bad_lines = False,
                         encoding="ISO-8859-1")
passwords = pswd_data.iloc[0:100,1]
passwords = passwords.to_frame()
passwords = passwords.astype(str)
count = 0
for count in passwords.index:
    count = count + 1
    
print(count)


'''
pswd_data.dropna(inplace = True)
with open("rockyou.txt", 'r') as f:
    lines = f.read().splitlines()
    last_line = lines[-1]
    print (last_line)
'''

sequence = 0
customer1 = 0
customer2 = 0
customer3 = 0
customer4 = 0
customer5 = 0
customer6 = 0
customer7 = 0
customer8 = 0
customer9 = 0
array = []
while sequence != count:
    password = passwords.iloc[sequence, 0]
    
    
    #first part to classify the customers 
    password_length_good = check_password_length(password)
    UpperLength = check_password_uppercase(password)
    digits = check_password_numbers(password)
    matchedPass = check_common_passwords(password)
    i=password_eval(password, password_length_good, UpperLength, digits, matchedPass)
    
    if i == 1:
        customer1 = customer1 + 1
    elif i == 2:
        customer2 = customer2 + 1
    elif i == 3:
        customer3 = customer3 + 1
    elif i == 4:
        customer4 = customer4 + 1
    elif i == 5:
        customer5 = customer5 + 1
    elif i == 6:
        customer6 = customer6 + 1
    elif i == 7:
        customer7 = customer7 + 1
    elif i == 8:
        customer8 = customer8 + 1
    elif i == 9:
        customer9 = customer9 + 1
       
    
        
    sequence = sequence + 1
#a = passwords.iloc[669878,0]
#print(a)

customer = [customer1,customer2, customer3, customer4,customer5,customer6, customer7, customer8,customer9]

array = makeArrays(customer)
array = pd.DataFrame(array)

y = array.iloc[1: ,0] #good plt
x = array.iloc[1: ,1]

plt.plot(x, y, label='Cusomters')
plt.xlabel('kind')
plt.ylabel('people number')
plt.title('people kind ')
plt.legend()
plt.show()


y1 = array.iloc[1: 4,0].tolist()
x1 = array.iloc[1: 4,1].tolist()
y2 = array.iloc[4: 10, 0].tolist()
x2 = array.iloc[4: 10, 1].tolist()

print("careful customers, ",customer1, "                   ,percentage :",(customer1/count)*100,"%")
print("digit-liked customers, ",customer2, "               ,percentage :",(customer2/count)*100,"%")
print("Upper-case obese customers, ",customer3, "          ,percentage :",(customer3/count)*100,"%")
print("abnormal and long-liked customers, ",customer4, "   ,percentage :",(customer4/count)*100,"%")
print("condensed and short-like customers, ",customer5, "  ,percentage :",(customer5/count)*100,"%")
print("digit-liked and short customers, ",customer6, "     ,percentage :",(customer6/count)*100,"%")
print("Uppercase-liked and short customers, ",customer7, " ,percentage :",(customer7/count)*100,"%")
print("Abnormal and short  customers, ",customer8, "       ,percentage :",(customer8/count)*100,"%")
print("careless and lazy customers, ",customer9, "         ,percentage :",(customer9/count)*100,"%")

plt.bar(x1, y1, label = '1:4 customers')
plt.bar(x2, y2, label = '4:9 customers')

plt.xlabel('kind')
plt.ylabel('people number')
plt.title('people kind ')
plt.legend()
plt.show()           #bad plt