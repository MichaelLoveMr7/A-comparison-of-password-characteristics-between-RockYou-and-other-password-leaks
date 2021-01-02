#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 15:14:40 2020

@author: yujiedong
"""

import pandas as pd
import numpy as np

RockYou = pd.read_csv("/Users/yujiedong/Downloads/BreachCompilation/data/rockyou.txt", 
                        header = None, error_bad_lines = False,
                        encoding="ISO-8859-1", engine = 'python')

combined_Random = pd.read_csv("/Users/yujiedong/Downloads/BreachCompilation/data/combined_Random.txt", 
                        sep = ":",header = None, error_bad_lines = False,
                        encoding="ISO-8859-1", engine = 'python')


RockYou_len = len(RockYou)
combined_Random_len = len(combined_Random)

print(RockYou.iloc[1])

i = 0
j = 0
i_eff = 0
while(i < RockYou_len):
    j = 0
    R = str(RockYou.iloc[i])
    while(j < combined_Random_len):
        C = str(combined_Random.iloc[j])
        if R == C:
            i_eff = i_eff + 1
            print("i_eff: ",i_eff)
        j = j + 1
        #print("j: ",j)
        
    i = i + 1
    print("i: ", i)