#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 15:51:47 2020

@author: yujiedong
"""
import sys, math, re
def check_password_length(password):
    length = len(str(password))
    
    password_length_good = True
    if type(password) == float:
        pass
    
    if length < 8:
        
        password_length_good = False
    
    else:
        
        password_length_good = True
    return password_length_good

def check_password_uppercase(password):
    UpperLength = 0
   
    UpperLength = len(re.findall(r'[A-Z]',str (password)))# problem here
    
    return UpperLength
                 
  
def check_password_numbers(password):
    digits = 0
    digits = len(re.findall(r'[0-9]', str(password)))
    return digits
   
        
def check_common_passwords(password):
    matchedPass = False
    commonPasswords = ['pssword','letmein','football','dragon','lemon','qwerty']
    
    for commonPass in commonPasswords:
        if commonPass == password:
            matchedPass = True
            
    return matchedPass
        
def password_eval(password, password_length_good, UpperLength, digits, matchedPass):
    print('\n[*] Password Evaluation: ')
    judge = 0
   
    if password_length_good == True and UpperLength >= 3 and digits >=3 and matchedPass == False:
        judge = 1
        print('careful customers')
    
    elif password_length_good == True and UpperLength <= 3 and digits >= 3 and matchedPass == False:
        judge = 2
        print('digit-liked customers')
        
    elif password_length_good == True and UpperLength >= 3 and digits <= 3 and matchedPass == False:
        judge = 3
        print('Upper-case liked customers')
        
    elif password_length_good == True and UpperLength <= 3 and digits <= 3 and matchedPass == False:
        judge = 4
        print('abnormal and long-password liked customers')
        
    elif password_length_good == False and UpperLength >= 3 and digits >= 3 and matchedPass == False:
        judge = 5
        print('condensed and short-like customers')
        
    elif password_length_good == False and UpperLength <= 3 and digits >= 3 and matchedPass == False:
        judge = 6
        print('digit-liked and short customers')
        
    elif password_length_good == False and UpperLength >= 3 and digits <= 3 and matchedPass == False:
        judge = 7
        print('Uppercase-liked and short customers')
    
    elif password_length_good == False and UpperLength <= 3 and digits <=3 and matchedPass == False:
        judge = 8
        print('Abnormal and short  customers')
        
    elif matchedPass == True:
        judge = 9
        print('careless and lazy customers')
    
    
        
    print(judge)
    return judge
'''

def file_len(fname):             #96-100 stackflow
    with open(fname) as f:
        for i,l in enumerate(f):
            pass
    return i + 1
'''

    
    
def makeArrays(customer):
    arrays = []
    arrays.append(("percentage", "kind"))
    a = 0
    for i in customer:
        
        a = a + 1
        arrays.append((i, a))
        
    return arrays






