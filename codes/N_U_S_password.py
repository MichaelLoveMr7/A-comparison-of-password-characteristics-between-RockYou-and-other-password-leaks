#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:27:17 2020

@author: yujiedong
"""

import re
'''
# for test
password= "uu"
length = 2
N_1_to_last2 = 0
U_1_to_last2 = 0
S_1_to_last2 = 0
row = 0
while(row < length -1) :
       if re.search('[0-9]', password[row]) :
           N_1_to_last2 = N_1_to_last2 + 1
           
       elif re.search('[A-Z]', password[row]):
           U_1_to_last2 = U_1_to_last2 + 1
           
       elif re.search('[a-z]', password[row]):
           pass
       
       else:
           S_1_to_last2 = S_1_to_last2 + 1
       row = row + 1
           
 #  return N_1_to_last2, U_1_to_last2, S_1_to_last2
'''
def N_U_S_password_0toLast(password, length):
   N_0_to_last = 0
   U_0_to_last = 0
   S_0_to_last = 0
   row = 0
   while(row < length) :
       if re.search('[0-9]', password[row]) :
           N_0_to_last = N_0_to_last + 1
           
       elif re.search('[A-Z]', password[row]):
           U_0_to_last = U_0_to_last + 1
           
       elif re.search('[a-z]', password[row]):
           pass
       
       else:
           S_0_to_last = S_0_to_last + 1
           
   return N_0_to_last, U_0_to_last, S_0_to_last


def N_U_S_ALL_password(password, length):
   N_1_to_last2 = 0
   U_1_to_last2 = 0
   S_1_to_last2 = 0
   row = 1
   while(row < length -1) :
       if re.search('[0-9]', password[row]) :
           N_1_to_last2 = N_1_to_last2 + 1
           
       elif re.search('[A-Z]', password[row]):
           U_1_to_last2 = U_1_to_last2 + 1
           
       elif re.search('[a-z]', password[row]):
           pass
       
       else:
           S_1_to_last2 = S_1_to_last2 + 1
           
   return N_1_to_last2, U_1_to_last2, S_1_to_last2
           
def N_U_S_password_odd_even(password, length):
    N1, N3, U1, U3, S1, S3 = 0, 0, 0, 0, 0, 0
        #For the first character is a capitalized letter
    if re.search('[A-Z]', password[0]):
        #print("first character Upper case")
        U1 = U1 + 1
        #print("U1", U1)
    
    # For the first character is a number
    elif re.search('[0-9]', password[0]):
        
        #print("first character Number ")
        N1 = N1 + 1
        #print("N1", N1)
        
    elif re.search('[a-z]', password[0]):
        pass
        #print("first character lower case")
        
    # For the first character is a special symbols    
    else:
        
        #print("first character special symbols or other things")
        #print(password[0])
        S1 = S1 + 1
        #print("S1", S1)
        
    #For the first character is a capitalized letter
    if re.search('[A-Z]', password[length-1]):
        #print("Last character Upper case")
        U3 = U3 + 1
        #print("U3", U3)
    
    # For the first character is a number
    elif re.search('[0-9]', password[length-1]):
        #print("Last character Number ")
        N3 = N3 + 1
        #print("N3", N3)
        
    elif re.search('[a-z]', password[length-1]):
        pass
        #print("Last character lower case")
        
    # For the first character is a special symbols    
    else:
        #print("Last character special symbols or other things")
        #print(password[length-1])
        S3 = S3 + 1
        #print("S3", S3)
     

    
    return N1, N3, U1, U3, S1, S3

def N_U_S_password_odd(password,length):
    N1, N2, N3, U1, U2, U3, S1, S2, S3 = 0, 0, 0, 0, 0, 0, 0, 0, 0

    length_odd_half = 0
    
    
    
    #For the first character is a capitalized letter
    if re.search('[A-Z]', password[0]):
        #print("first character Upper case")
        U1 = U1 + 1
        #print("U1", U1)
    
    # For the first character is a number
    elif re.search('[0-9]', password[0]):
        
        #print("first character Number ")
        N1 = N1 + 1
        #print("N1", N1)
        
    elif re.search('[a-z]', password[0]):
        pass
        #print("first character lower case")
        
    # For the first character is a special symbols    
    else:
        
        #print("first character special symbols or other things")
        #print(password[0])
        S1 = S1 + 1
        #print("S1", S1)
       
        
    
    #Prepare for finding out what is in the half of the password
    #length=len(password)
    #print(length)
    
     

        
    length_odd_half = int((length-1)/2)  

    #print("length_odd_half",length_odd_half)
    
#Whether the character in half is capital or not
    if re.search('[A-Z]', password[length_odd_half] ):
        #print("The part of character in half is upper case")
        U2 = U2 + 1
        #print("U2 odd", U2)
        #print(password[length_odd_half])
        
    elif re.search('[0-9]', password[length_odd_half] ):
        #print("The part of characters in half is number")
        N2 = N2 + 1
        #print("N2 odd", N2)
        #print(password[length_odd_half])
        
    elif re.search('[a-z]', password[length_odd_half]):
        pass
        #print("The part of characters in half is lower case") 
        #print(password[length_odd_half ])
    
    else:
        #print("The part of characters in half is special symbol")
        S2 = S2 + 1
        #print("S2 odd", S2)
        #print(password[length_odd_half])
    
    #For the first character is a capitalized letter
    if re.search('[A-Z]', password[length-1]):
        #print("Last character Upper case")
        U3 = U3 + 1
        #print("U3", U3)
    
    # For the first character is a number
    elif re.search('[0-9]', password[length-1]):
        #print("Last character Number ")
        N3 = N3 + 1
        #print("N3", N3)
        
    elif re.search('[a-z]', password[length-1]):
        pass
        #print("Last character lower case")
        
    # For the first character is a special symbols    
    else:
        #print("Last character special symbols or other things")
        #print(password[length-1])
        S3 = S3 + 1
        #print("S3", S3)
     

    
    return N1, N2, N3, U1, U2, U3, S1, S2, S3

def N_U_S_password_even(password,length):
    N1_EVEN, N2_EVEN, N3_EVEN, U1_EVEN, U2_EVEN, U3_EVEN, S1_EVEN, S2_EVEN, S3_EVEN = 0, 0, 0, 0, 0, 0, 0, 0, 0 
    length_even_half = 0, 0
    
    
    
    #For the first character is a capitalized letter
    if re.search('[A-Z]', password[0]):
        #print("first character Upper case")
        U1_EVEN= U1_EVEN + 1
        #print("U1", U1)
    
    # For the first character is a number
    elif re.search('[0-9]', password[0]):
        
        #print("first character Number ")
        N1_EVEN = N1_EVEN + 1
        #print("N1", N1)
        
    elif re.search('[a-z]', password[0]):
        pass
        #print("first character lower case")
        
    # For the first character is a special symbols    
    else:
        
        #print("first character special symbols or other things")
        #print(password[0])
        S1_EVEN = S1_EVEN + 1
        #print("S1", S1)
       
        
    
    #Prepare for finding out what is in the half of the password
    #length=len(password)
    #print(length)
    
    #The even-number half length 
    
    length_even_half = int(length / 2)-1
    #print(length_even_half)
    
#Whether the character in half is capital or not
    if re.search('[A-Z]', password[length_even_half] ):
        #print("The part of character in half is upper case")
        U2_EVEN = U2_EVEN + 1
        #print("U2", U2)
        #print(password[length_even_half])
        
    elif re.search('[0-9]', password[length_even_half] ):
        #print("The part of characters in half is number")
        N2_EVEN = N2_EVEN + 1
        #print("N2", N2)
        #print(password[length_even_half])
        
    elif re.search('[a-z]', password[length_even_half]):
        pass
        #print("The part of characters in half is lower case") 
        #print(password[length_even_half + 1])
    
    else:
        #print("The part of characters in half is special symbol")
        S2_EVEN = S2_EVEN + 1
        #print("S2", S2)
        #print(password[length_even_half])
        
        
    if re.search('[A-Z]', password[length_even_half + 1] ):
        #print(password[length_even_half + 1])
        #print("The other part of character in half is upper case")
        U2_EVEN = U2_EVEN + 1
        #print("U2", U2)
        #print(password[length_even_half + 1])
        
    elif re.search('[0-9]', password[length_even_half + 1] ):
        #print("The other part of characters in half is number")
        N2_EVEN = N2_EVEN + 1
        #print("N2", N2)
        #print(password[length_even_half + 1])
        
    elif re.search('[a-z]', password[length_even_half + 1]):
        pass
        #print("The other part of characters in half is lower case") 
        #print(password[length_even_half + 1])
        
    else:
        #print("The other part of characters in half is special symbol")
        S2_EVEN = S2_EVEN + 1
        #print("S2", S2)
        #print(password[length_even_half + 1])
    
    
    #For the first character is a capitalized letter
    if re.search('[A-Z]', password[length-1]):
        #print("Last character Upper case")
        U3_EVEN = U3_EVEN + 1
        #print("U3", U3)
    
    # For the first character is a number
    elif re.search('[0-9]', password[length-1]):
        #print("Last character Number ")
        N3_EVEN = N3_EVEN + 1
        #print("N3", N3)
        
    elif re.search('[a-z]', password[length-1]):
        pass
        #print("Last character lower case")
        
    # For the first character is a special symbols    
    else:
        #print("Last character special symbols or other things")
        #print(password[length-1])
        S3_EVEN = S3_EVEN + 1
        #print("S3", S3)
     

    
    return N1_EVEN, N2_EVEN, N3_EVEN, U1_EVEN, U2_EVEN, U3_EVEN, S1_EVEN, S2_EVEN, S3_EVEN
    




                 