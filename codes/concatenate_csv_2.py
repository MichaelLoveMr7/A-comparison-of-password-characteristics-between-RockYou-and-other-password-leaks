#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 23:20:25 2020

@author: yujiedong
"""

import glob
import os
import pandas as pd



os.chdir("/Users/yujiedong/Downloads/BreachCompilation/data/final results(1 to last2)/combined")

extension = 'csv'

all_filenames = [i for i in glob.glob('*.{}'.format(extension))] # ?


# combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
# export to csv

# combine all files in the list

data = combined_csv.iloc[:,1:3]
data = data.reset_index(drop=True)
#data.to_csv('process_0aANDlast2.csv', encoding='utf-8-sig')



#reopen combined_csv.csv


count = 0

N_1_to_last2_ALL_SUM = 0
U_1_to_last2_ALL_SUM = 0
S_1_to_last2_ALL_SUM = 0
User_count_SUM = 0
length_password_ALL_SUM = 0

count_users = 0
count = 0

data = combined_csv.iloc[:,1:3]
data = data.reset_index(drop=True)
length_csv = len(data)

#print(data.iloc[599,2])
#print(data)




'''
i = 0
while(count < length_csv):
    if data.iloc[count,0] == 'User_count(for count in passwords.index)':
        #print('count_odd_even:',data.iloc[count, 1])
        print('User_count:',data.iloc[count,1])
        i = i + 1
    count = count + 1
print("i:",i)
'''
i = 0 
j = 0
x = 0
y = 0
z = 0
while(count < length_csv):
    print()
    print('count:',count)
    if data.iloc[count, 0] == "User_count(for count in passwords.index)":
        User_count_SUM = User_count_SUM + data.iloc[count,1]
        #print()
        #print("User_count_singular",data.iloc[count,1])
        #print('User_count_SUM:',User_count_SUM)

        i = i + 1
        print("i", i)
#    if count == 599:
#        print("important",data.iloc[count,1])
#        break
    
    if data.iloc[count, 0] == "N_1_to_last2_ALL":
        N_1_to_last2_ALL_SUM = N_1_to_last2_ALL_SUM + data.iloc[count,1]
        #print(ALL_ODD)
        #print()
        #print("User_count_singular",data.iloc[count,1])
        #print('User_count_SUM:',User_count_SUM)
        j = j + 1
        print("j", j)
        
    if data.iloc[count, 0] == "U_1_to_last2_ALL":
        U_1_to_last2_ALL_SUM = U_1_to_last2_ALL_SUM + data.iloc[count,1]
        x = x + 1
        print("x", x)
        #print(ALL_ODD)
        
    if data.iloc[count, 0] == "S_1_to_last2_ALL" :
        #print(data.iloc[count, 1])
        S_1_to_last2_ALL_SUM = S_1_to_last2_ALL_SUM + data.iloc[count, 1]
        y = y + 1
        print("y", y)
        
        
    if data.iloc[count, 0] == 'length_ALL(= length_ALL + len(password))':
        length_password_ALL_SUM = length_password_ALL_SUM + data.iloc[count, 1]
        z = z + 1
        print("z", z)
        
        #np.savetxt('ALL.csv', (data.iloc[count,1]))
        #print(count,data.iloc[count, 1])
    count = count + 1
print('count',count) 
print('User_count_SUM',User_count_SUM)
print("i", i)
print("j", j)
print("x", x)
print("y", y)
print("z", z)


N_1_to_last2_ALL_SUM_AVERAGE = N_1_to_last2_ALL_SUM/length_password_ALL_SUM
U_1_to_last2_ALL_SUM_AVERAGE = U_1_to_last2_ALL_SUM/length_password_ALL_SUM
S_1_to_last2_ALL_SUM_AVERAGE = S_1_to_last2_ALL_SUM/length_password_ALL_SUM


N_1_to_last2_ALL_SUM = ['N_1_to_last2_ALL_SUM:',N_1_to_last2_ALL_SUM]
U_1_to_last2_ALL_SUM = ['U_1_to_last2_ALL_SUM:',U_1_to_last2_ALL_SUM]
S_1_to_last2_ALL_SUM = ['S_1_to_last2_ALL_SUM:',S_1_to_last2_ALL_SUM]
N_1_to_last2_ALL_SUM_AVERAGE = ['N_1_to_last2_ALL_SUM/length_password_ALL_SUM:',N_1_to_last2_ALL_SUM_AVERAGE]
U_1_to_last2_ALL_SUM_AVERAGE = ['U_1_to_last2_ALL_SUM/length_password_ALL_SUM:',U_1_to_last2_ALL_SUM_AVERAGE]
S_1_to_last2_ALL_SUM_AVERAGE = ['S_1_to_last2_ALL_SUM/length_password_ALL_SUM:',S_1_to_last2_ALL_SUM_AVERAGE]
length_password_ALL_SUM =['length_password_ALL_SUM:',length_password_ALL_SUM]
User_count_SUM = ['User_count_SUM:',User_count_SUM]

import numpy as np
np.savetxt('combined_13B_1TOlast2.csv', (  
                                  User_count_SUM,
                                  N_1_to_last2_ALL_SUM,
                                  U_1_to_last2_ALL_SUM,
                                  S_1_to_last2_ALL_SUM,
                                  length_password_ALL_SUM,
                                  N_1_to_last2_ALL_SUM_AVERAGE,
                                  U_1_to_last2_ALL_SUM_AVERAGE,
                                  S_1_to_last2_ALL_SUM_AVERAGE), fmt='%s')
result_data=pd.read_csv('combined_13B_1TOlast2.csv',sep=":",header = None)
result_data.to_csv('combined_13B_1TOlast2.csv')
#data.to_csv('check_again.csv')

'''
count = 0
for count in data.index:
        if count == 1:
            print(count)
            print(data.iloc[count,1])
        count = count + 1
'''
'''
print(data)     
count = 0
dataLen = len(data)
cycle = 0


while(count < dataLen):
    
    if(cycle == 19):
        cycle = 0
    
    data.iloc[count, 0] = "count_odd"
    cycle = cycle + 1
    count= count + 1
    
    data.iloc[count, 0] = "N1ALL_ODD"
    cycle = cycle + 1
    count= count + 1
    
    data.iloc[count, 0] = "N2ALL_ODD"
    cycle = cycle + 1
    count= count + 1
    
    data.iloc[count, 0] = "N3ALL_ODD"
    cycle = cycle + 1
    count= count + 1
    #if cycle == 4:
    
    data.iloc[count, 0] = "U1ALL_ODD"
    cycle = cycle + 1
    count= count + 1
    
#if cycle == 5:
    data.iloc[count, 0] = "U2ALL_ODD"
    cycle = cycle + 1
    count= count + 1
    
#if cycle == 6:
    data.iloc[count, 0] = "U3ALL_ODD"
    cycle = cycle + 1
    count= count + 1
    
#if cycle == 7:
    data.iloc[count, 0] = "S1ALL_ODD"
    cycle = cycle + 1
    count= count + 1
    
#if cycle == 8:
    data.iloc[count, 0] = "S2ALL_ODD"
    cycle = cycle + 1
    count= count + 1
    
#if cycle == 9:
    data.iloc[count, 0] = "S3ALL_ODD"
    cycle = cycle + 1
    count= count + 1
   # count= count + 1
    
#if cycle > 9 and cycle < 13:
    data.iloc[count, 0] = "count_even"
    cycle = cycle + 1
    count= count + 1

    data.iloc[count, 0] = "N1ALL_EVEN"
    cycle = cycle + 1
    count= count + 1
    
    data.iloc[count, 0] = "N2ALL_EVEN"
    cycle = cycle + 1
    count= count + 1
    
    data.iloc[count, 0] = "N3ALL_EVEN"
    cycle = cycle + 1
    count= count + 1    
    
#if cycle == 14:
    data.iloc[count, 0] = "U1ALL_EVEN"
    cycle = cycle + 1
    count= count + 1
    
#if cycle == 15:
    data.iloc[count, 0] = "U2ALL_EVEN"
    cycle = cycle + 1
    count= count + 1
    
#if cycle == 16:
    data.iloc[count, 0] = "U3ALL_EVEN"
    cycle = cycle + 1
    count= count + 1
    
#if cycle == 17:
    data.iloc[count, 0] = "S1ALL_EVEN"
    cycle = cycle + 1
    count= count + 1
    
#if cycle == 18:
    data.iloc[count, 0] = "S2ALL_EVEN"
    cycle = cycle + 1
    count= count + 1
    
#if cycle == 19:
    data.iloc[count, 0] = "S3ALL_EVEN"     
    cycle = cycle + 1
    count= count + 1
    
  #  if(data.iloc[count, 1] < data.iloc[count-1, 2]):
  #      print("BIG PROBLEMS",count)
        
    
print(data)   
data = pd.DataFrame(data)
data.to_csv("data_ALL_rockyou.csv",index=False, encoding='utf-8-sig')
'''





'''


print(i)
print(N2ALL)
print(U2ALL)
print(S2ALL)
ALL = 0
ALL = ALL_EVEN + ALL_ODD
print("the number of ODD length passwords: ",ALL_ODD)
print("the number of EVEN length passwords:",ALL_EVEN)
print("ALL passwords                      :",ALL)


print("'[0-9]', password[0]                 :",N1ALL, "Percentage", (N1ALL/ALL)*100,"%")
print("'[0-9]', password[length_half]       :",N2ALL, "Percentage", (N2ALL/ALL)*100,"%")
print("'[0-9]', password[length-1]          :",N3ALL, "Percentage", (N3ALL/ALL)*100,"%")
print("'[A-Z]', password[0]                 :",U1ALL, "Percentage", (U1ALL/ALL)*100,"%")
print("'[A-Z]', password[length_half]       :",U2ALL, "Percentage", (U2ALL/ALL)*100,"%")
print("'[A-Z]', password[length-1]          :",U3ALL, "Percentage", (U3ALL/ALL)*100,"%")
print("Special symbol, password[0]          :",S1ALL, "Percentage", (S1ALL/ALL)*100,"%")
print("Special symbol, password[length_half]:",S2ALL, "Percentage", (S2ALL/ALL)*100,"%")
print("Special symbol, password[length-1]   :",S3ALL, "Percentage", (S3ALL/ALL)*100,"%")

from CUS_0to9 import makeArrays
import matplotlib.pyplot as plt
password_characteristics = [N1ALL, N2ALL, N3ALL,U1ALL,U2ALL,U3ALL,S1ALL,S2ALL,S3ALL]

array = makeArrays(password_characteristics)
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
plt.title(' password characteristics ')
plt.legend()
plt.show() 
'''     