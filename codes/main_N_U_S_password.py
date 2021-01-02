#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 14:15:58 2020

@author: yujiedong
"""
import os
os.getcwd()
os.chdir("/Users/yujiedong/Downloads/BreachCompilation/data")

from N_U_S_password import N_U_S_password_odd, N_U_S_password_even, N_U_S_ALL_password
import numpy as np
import pandas as pd
from CUS_0to9 import makeArrays
#import matplotlib.pyplot as plt
#from astropy.visualization import hist
#from zxcvbn import zxcvbn

pswd_data = pd.read_csv("/Users/yujiedong/Downloads/BreachCompilation/data/rockyou.txt", 
                        sep=":", header = None, error_bad_lines = False,
                        encoding="ISO-8859-1", engine = 'python')
#print(pswd_data.iloc[:2300000,1])
passwords = pswd_data.iloc[:,0]

passwords = passwords.to_frame()
passwords = passwords.astype(str)
#print(passwords)
count = 0
for count in passwords.index:
        count = count + 1
        

N1ALL_ODD, N2ALL_ODD, N3ALL_ODD = 0, 0, 0
U1ALL_ODD, U2ALL_ODD, U3ALL_ODD = 0, 0, 0
S1ALL_ODD, S2ALL_ODD, S3ALL_ODD = 0, 0, 0

N1ALL_EVEN, N2ALL_EVEN, N3ALL_EVEN = 0, 0, 0
U1ALL_EVEN, U2ALL_EVEN, U3ALL_EVEN = 0, 0, 0
S1ALL_EVEN, S2ALL_EVEN, S3ALL_EVEN = 0, 0, 0

row = 0
count_odd_even = 0
#count_odd = 0
#count_even = 0
'''
N_1_to_last2_ALL = 0
U_1_to_last2_ALL = 0
S_1_to_last2_ALL = 0
N_1_to_last2_ALL_percent = 0
U_1_to_last2_ALL_percent = 0
S_1_to_last2_ALL_percent = 0
'''
length_ALL = 0
#zxcvbn_ALL = 0
while row != count:
    password = passwords.iloc[row, 0]
    #get the zxcvbn score
    #zxcvbn_results=zxcvbn(password)
    #zxcvbn_score = zxcvbn_results.get('score')
    #print('zxcvbn_score',zxcvbn_score)
    #zxcvbn_ALL = zxcvbn_ALL + zxcvbn_score
    
    length = len(password)
    '''
    N_1_to_last2_percent, U_1_to_last2_percent, S_1_to_last2_percent, N_1_to_last2, U_1_to_last2, S_1_to_last2 = N_U_S_ALL_password(password, length)
    N_1_to_last2_ALL = N_1_to_last2_ALL + N_1_to_last2
    U_1_to_last2_ALL = U_1_to_last2_ALL + U_1_to_last2
    S_1_to_last2_ALL = S_1_to_last2_ALL + S_1_to_last2
    
    N_1_to_last2_ALL_percent = N_1_to_last2_ALL_percent + N_1_to_last2_percent
    U_1_to_last2_ALL_percent = U_1_to_last2_ALL_percent + U_1_to_last2_percent
    S_1_to_last2_ALL_percent = S_1_to_last2_ALL_percent + S_1_to_last2_percent
    length_ALL = length_ALL + length
    #print(row)
    
    '''
    '''
    if length% 2 == 1:
        N1, N2, N3, U1, U2, U3, S1, S2, S3 = N_U_S_password_odd(password,length)
    
        N1ALL_ODD = N1ALL_ODD + N1
        #print(N1ALL)
        N2ALL_ODD = N2ALL_ODD + N2
        N3ALL_ODD = N3ALL_ODD + N3
        U1ALL_ODD = U1ALL_ODD + U1
        U2ALL_ODD = U2ALL_ODD + U2
        U3ALL_ODD = U3ALL_ODD + U3
        S1ALL_ODD = S1ALL_ODD + S1
        S2ALL_ODD = S2ALL_ODD + S2
        S3ALL_ODD = S3ALL_ODD + S3
        count_odd = count_odd + 1
        
    else:
        N1_EVEN, N2_EVEN, N3_EVEN, U1_EVEN, U2_EVEN, U3_EVEN, S1_EVEN, S2_EVEN, S3_EVEN = N_U_S_password_even(password,length)
        N1ALL_EVEN = N1ALL_EVEN + N1_EVEN
        N2ALL_EVEN = N2ALL_EVEN + N2_EVEN
        N3ALL_EVEN = N3ALL_EVEN + N3_EVEN
        U1ALL_EVEN = U1ALL_EVEN + U1_EVEN
        U2ALL_EVEN = U2ALL_EVEN + U2_EVEN
        U3ALL_EVEN = U3ALL_EVEN + U3_EVEN
        S1ALL_EVEN = S1ALL_EVEN + S1_EVEN
        S2ALL_EVEN = S2ALL_EVEN + S2_EVEN
        S3ALL_EVEN = S3ALL_EVEN + S3_EVEN
        count_even = count_even + 1
    '''  
    '''
    print("N_1_to_last2_ALL_percent",N_1_to_last2_ALL_percent)
    print("U_1_to_last2_ALL_percent",U_1_to_last2_ALL_percent)
    print("S_1_to_last2_ALL_percent",S_1_to_last2_ALL_percent)
    print()
    '''
    N1, N2, N3, U1, U2, U3, S1, S2, S3 = N_U_S_password_odd(password,length)

    N1ALL_ODD = N1ALL_ODD + N1
    #print(N1ALL)
    N2ALL_ODD = N2ALL_ODD + N2
    N3ALL_ODD = N3ALL_ODD + N3
    U1ALL_ODD = U1ALL_ODD + U1
    U2ALL_ODD = U2ALL_ODD + U2
    U3ALL_ODD = U3ALL_ODD + U3
    S1ALL_ODD = S1ALL_ODD + S1
    S2ALL_ODD = S2ALL_ODD + S2
    S3ALL_ODD = S3ALL_ODD + S3
    count_odd = count_odd + 1
    
    row = row + 1
'''
print("out")    
print("N_1_to_last2_ALL_percent:",N_1_to_last2_ALL_percent)
print("U_1_to_last2_ALL_percent:",U_1_to_last2_ALL_percent)
print("S_1_to_last2_ALL_percent:",S_1_to_last2_ALL_percent)
print()
'''
'''
N_1_to_last2_ALL_percent_average = N_1_to_last2_ALL_percent/count
U_1_to_last2_ALL_percent_average = U_1_to_last2_ALL_percent/count
S_1_to_last2_ALL_percent_average = S_1_to_last2_ALL_percent/count

N_1_to_last2_ALL_percent = N_1_to_last2_ALL/length_ALL
U_1_to_last2_ALL_percent = U_1_to_last2_ALL/length_ALL
S_1_to_last2_ALL_percent = S_1_to_last2_ALL/length_ALL
'''
#zxcvbn_average = zxcvbn_ALL/count
'''    
print("N_1_to_last2_ALL_percent_average:", N_1_to_last2_ALL_percent_average)
print("U_1_to_last2_ALL_percent_average:", U_1_to_last2_ALL_percent_average)
print("S_1_to_last2_ALL_percent_average:", S_1_to_last2_ALL_percent_average)
print("customer count", count)
'''
'''
N_1_to_last2_ALL_percent_average = ["N_1_to_last2_ALL_Users_percent/User count:", N_1_to_last2_ALL_percent_average]
U_1_to_last2_ALL_percent_average = ["U_1_to_last2_ALL_Users_percent/User count:", U_1_to_last2_ALL_percent_average]
S_1_to_last2_ALL_percent_average = ["S_1_to_last2_ALL_Users_percent/User count:", S_1_to_last2_ALL_percent_average]
count = ["User_count(for count in passwords.index):", count]
#zxcvbn_ALL = ["zxcvbn_ALL:",zxcvbn_ALL]
N_1_to_last2_ALL = ["N_1_to_last2_ALL:",N_1_to_last2_ALL]
U_1_to_last2_ALL = ["U_1_to_last2_ALL:",U_1_to_last2_ALL]
S_1_to_last2_ALL = ["S_1_to_last2_ALL:",S_1_to_last2_ALL]
length_ALL = ["length_ALL(= length_ALL + len(password)):", length_ALL]

#zxcvbn_average = ["zxcvbn_average:",zxcvbn_average]
N_1_to_last2_ALL_percent = ["N_1_to_last2_ALL/length_ALL:",N_1_to_last2_ALL_percent]
U_1_to_last2_ALL_percent = ["U_1_to_last2_ALL/length_ALL:",U_1_to_last2_ALL_percent]
S_1_to_last2_ALL_percent = ["S_1_to_last2_ALL/length_ALL:",S_1_to_last2_ALL_percent]


np.savetxt('scores_combined_z.csv', (   N_1_to_last2_ALL_percent_average,
                                     U_1_to_last2_ALL_percent_average,
                                     S_1_to_last2_ALL_percent_average,
                                  count, #zxcvbn_ALL,
                                  N_1_to_last2_ALL,
                                  U_1_to_last2_ALL,
                                  S_1_to_last2_ALL,
                                  length_ALL, #zxcvbn_average,
                                  N_1_to_last2_ALL_percent,
                                  U_1_to_last2_ALL_percent,
                                  S_1_to_last2_ALL_percent), fmt='%s')
result_data=pd.read_csv('scores_combined_z.csv',sep=":",header = None)
result_data.to_csv('scores_combined_z.csv')

'''
print("N1ALL_ODD",N1ALL_ODD," N2ALL_ODD",N2ALL_ODD, "N3ALL_ODD", N3ALL_ODD,
      "U1ALL_ODD", U1ALL_ODD,"U2ALL_ODD",U2ALL_ODD, 
  "U3ALL_ODD", U3ALL_ODD,"S1ALL_ODD",S1ALL_ODD,
  "S2ALL_ODD", S2ALL_ODD,"S3ALL_ODD",S3ALL_ODD) 
print("N1ALL_EVEN",N1ALL_EVEN," N2ALL_EVEN",N2ALL_EVEN, "N3ALL_EVEN", N3ALL_EVEN,
      "U1ALL_EVEN", U1ALL_EVEN,"U2ALL_EVEN",U2ALL_EVEN, 
  "U3ALL_EVEN", U3ALL_EVEN,"S1ALL_EVEN",S1ALL_EVEN,
  "S2ALL_EVEN", S2ALL_EVEN,"S3ALL_EVEN",S3ALL_EVEN) 
'''
'''
print(count_odd)
print(count_even)
'''


'''

#print(the result of ODD passwords)
password_characteristics_ODD = [N1ALL_ODD, N2ALL_ODD, N3ALL_ODD, U1ALL_ODD, 
                            U2ALL_ODD, U3ALL_ODD, S1ALL_ODD, S2ALL_ODD, S3ALL_ODD]

print("the number of ODD length passwords in z folder :", count_odd)
print("'[0-9]', password[0]:",N1ALL_ODD, "                     ,percentage :",(N1ALL_ODD/count_odd)*100,"%")
print("'[0-9]', password[length_odd_half]:",N2ALL_ODD, "       ,percentage :",(N2ALL_ODD/count_odd)*100,"%")
print("'[0-9]', password[length-1]:",N3ALL_ODD, "              ,percentage :",(N3ALL_ODD/count_odd)*100,"%")
print("'[A-Z]', password[0]:",U1ALL_ODD, "                     ,percentage :",(U1ALL_ODD/count_odd)*100,"%")
print("'[A-Z]', password[length_odd_half]:",U2ALL_ODD, "       ,percentage :",(U2ALL_ODD/count_odd)*100,"%")
print("'[A-Z]', password[length-1]:",U3ALL_ODD, "              ,percentage :",(U3ALL_ODD/count_odd)*100,"%")
print("Special symbol,password[0]:",S1ALL_ODD, "               ,percentage :",(S1ALL_ODD/count_odd)*100,"%")
print("Special symbol,password[length_odd_half]:",S2ALL_ODD, " ,percentage :",(S2ALL_ODD/count_odd)*100,"%")
print("Special symbol,password[length-1]:",S3ALL_ODD, "        ,percentage :",(S3ALL_ODD/count_odd)*100,"%")

# plot odd 
array = makeArrays(password_characteristics_ODD)
array = pd.DataFrame(array)

y = array.iloc[1: ,0] #good plt
x = array.iloc[1: ,1]


y1 = array.iloc[1: 4,0].tolist()
x1 = array.iloc[1: 4,1].tolist()
y2 = array.iloc[4: 7, 0].tolist()
x2 = array.iloc[4: 7, 1].tolist()
y3 = array.iloc[7: 10, 0].tolist()
x3 = array.iloc[7: 10, 1].tolist()

width = 0.7
plt.bar(x1, y1, width, label = 'Number ')
plt.bar(x2, y2, width, label = 'Upper case')
plt.bar(x3, y3, width, label = 'Special symbol ')


plt.xlabel('Number, Upper Case and Special Symbols from first, middle, end')
plt.ylabel(' Numbers')
plt.title(' z folder ODD length passwords ')
plt.legend()
plt.show()           #bad plt   
    




#print(the result of EVEN passwords)
password_characteristics_EVEN = [N1ALL_EVEN, N2ALL_EVEN, N3ALL_EVEN, U1ALL_EVEN, 
                            U2ALL_EVEN, U3ALL_EVEN, S1ALL_EVEN, S2ALL_EVEN, S3ALL_EVEN]

print("the number of EVEN length passwords in z folder:", count_even)
print("'[0-9]', password[0]:",N1ALL_EVEN, "                         ,percentage :",(N1ALL_EVEN/count_even)*100,"%")
print("'[0-9]', password[length_even_half](2):",N2ALL_EVEN, "       ,percentage :",(N2ALL_EVEN/(count_even*2))*100,"%")
print("'[0-9]', password[length-1]:",N3ALL_EVEN, "                  ,percentage :",(N3ALL_EVEN/count_even)*100,"%")
print("'[A-Z]', password[0]:",U1ALL_EVEN, "                         ,percentage :",(U1ALL_EVEN/count_even)*100,"%")
print("'[A-Z]', password[length_even_half](2):",U2ALL_EVEN, "       ,percentage :",(U2ALL_EVEN/(count_even*2))*100,"%")
print("'[A-Z]', password[length-1]:",U3ALL_EVEN, "                  ,percentage :",(U3ALL_EVEN/count_even)*100,"%")
print("Special symbol, password[0]:",S1ALL_EVEN, "                  ,percentage :",(S1ALL_EVEN/count_even)*100,"%")
print("Special symbol, password[length_even_half](2):",S2ALL_EVEN, ",percentage :",(S2ALL_EVEN/(count_even*2))*100,"%")
print("Special symbol, password[length-1]:",S3ALL_EVEN, "           ,percentage :",(S3ALL_EVEN/count_even)*100,"%")
    
#plot even
array = makeArrays(password_characteristics_EVEN)
array = pd.DataFrame(array)

y = array.iloc[1: ,0] #good plt
x = array.iloc[1: ,1]

y1 = array.iloc[1: 4,0].tolist()
x1 = array.iloc[1: 4,1].tolist()
y2 = array.iloc[4: 7, 0].tolist()
x2 = array.iloc[4: 7, 1].tolist()
y3 = array.iloc[7: 10, 0].tolist()
x3 = array.iloc[7: 10, 1].tolist()

width = 0.7
#ax = plt.subplots()
plt.bar(x1, y1, width, label = 'Number ')
plt.bar(x2, y2, width, label = 'Upper case')
plt.bar(x3, y3, width, label = 'Special symbol ')


plt.xlabel('Number, Upper Case and Special Symbols from first, middle, end')
plt.ylabel(' Numbers')
plt.title('z folder EVEN length passwords ')
plt.legend()
plt.show()

#Plot them all



count_odds = ['count_odd', count_odd ]
N1ALL_ODDS = ['N1ALL_ODD', N1ALL_ODD]
N2ALL_ODDS = ['N2ALL_ODD',  N2ALL_ODD]
N3ALL_ODDS = ['N3ALL_ODD',  N3ALL_ODD]
U1ALL_ODDS = ['U1ALL_ODD', U1ALL_ODD] # Change from N1ALL_ODD to U1ALL_ODD
U2ALL_ODDS = ['U2ALL_ODD',  U2ALL_ODD]
U3ALL_ODDS = ['U3ALL_ODD',  U3ALL_ODD]
S1ALL_ODDS = ['S1ALL_ODD', S1ALL_ODD]
S2ALL_ODDS = ['S2ALL_ODD',  S2ALL_ODD]
S3ALL_ODDS = ['S3ALL_ODD',  S3ALL_ODD]

count_evens = ['count_even', count_even ]
N1ALL_EVENS = ['N1ALL_EVEN', N1ALL_EVEN]
N2ALL_EVENS = ['N2ALL_EVEN',  N2ALL_EVEN]
N3ALL_EVENS = ['N3ALL_EVEN',  N3ALL_EVEN]
U1ALL_EVENS = ['U1ALL_EVEN', U1ALL_EVEN]
U2ALL_EVENS = ['U2ALL_EVEN',  U2ALL_EVEN]
U3ALL_EVENS = ['U3ALL_EVEN',  U3ALL_EVEN]
S1ALL_EVENS = ['S1ALL_EVEN', S1ALL_EVEN]
S2ALL_EVENS = ['S2ALL_EVEN',  S2ALL_EVEN]
S3ALL_EVENS = ['S3ALL_EVEN',  S3ALL_EVEN]

np.savetxt('scores_z.csv', (   count_odds, N1ALL_ODDS, N2ALL_ODDS, N3ALL_ODDS,
                                     U1ALL_ODDS, U2ALL_ODDS, U3ALL_ODDS,
                                     S1ALL_ODDS, S2ALL_ODDS, S3ALL_ODDS,
                                  count_evens, N1ALL_EVENS, N2ALL_EVENS, N3ALL_EVENS,
                                     U1ALL_EVENS, U2ALL_EVENS, U3ALL_EVENS,
                                     S1ALL_EVENS, S2ALL_EVENS, S3ALL_EVENS), fmt='%s')
result_data=pd.read_csv('scores_z.csv',sep=" ",header = None)
result_data.to_csv('scores_z.csv')
'''






