#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 14:04:14 2020

@author: yujiedong
"""

import numpy as np
import pandas as pd
import os
import re
os.getcwd()
os.chdir("/Users/yujiedong/Downloads/BreachCompilation/data")

pswd = pd.read_csv("q copy", 
                        sep=":", header = None, error_bad_lines = False,
                        encoding="ISO-8859-1", engine = 'python')



i = 0
array_0 = []
array_1 = []
array_2 = []
array_3 = []
array_4 = []
array_5 = []
array_6 = []
array_7 = []
array_8 = []
array_9 = []

array_a_A = []
array_b_B = []
array_c_C = []
array_d_D = []
array_e_E = []
array_f_F = []
array_g_G = []
array_h_H = []
array_i_I = []
array_j_J = []
array_k_K = []
array_l_L = []
array_m_M = []
array_n_N = []
array_o_O = []
array_p_P = []
array_q_Q = []
array_r_R = []
array_s_S = []
array_t_T = []
array_u_U = []
array_v_V = []
array_w_W = []
array_x_X = []
array_y_Y = []
array_z_Z = []

array_symbol = []

length_pswd = len(pswd)

while(i < length_pswd):
    password = pswd.iloc[i, 1]
    password = str(password)
    if password != 'None' and password != 'nan':
        
        #array.append(password)
        
        if re.search('0', password[0]):
            array_0.append(password)
            
        elif re.search('1', password[0]):
            array_1.append(password)
            
        elif re.search('2', password[0]): 
            array_2.append(password)
            
        elif re.search('3', password[0]):
            array_3.append(password)
            
        elif re.search('4', password[0]): 
            array_4.append(password)
            
        elif re.search('5', password[0]):
            array_5.append(password)
            
        elif re.search('6', password[0]): 
            array_6.append(password)
            
        elif re.search('7', password[0]):
            array_7.append(password)
            
        elif re.search('8', password[0]): 
            array_8.append(password)
            
        elif re.search('9', password[0]):
            array_9.append(password)
            
        elif re.search('a|A', password[0]):
            array_a_A.append(password)
            
        elif re.search('b|B', password[0]): 
            array_b_B.append(password)
            
        elif re.search('c|C', password[0]):
            array_c_C.append(password)
            
        elif re.search('d|D', password[0]): 
            array_d_D.append(password)
            
        elif re.search('e|E', password[0]):
            array_e_E.append(password)
            
        elif re.search('f|F', password[0]): 
            array_f_F.append(password)
            
        elif re.search('g|G', password[0]):
            array_g_G.append(password)
            
        elif re.search('h|H', password[0]): 
            array_h_H.append(password)
            
        elif re.search('i|I', password[0]):
            array_i_I.append(password)
            
        elif re.search('j|J', password[0]):
            array_j_J.append(password)
            
        elif re.search('k|K', password[0]): 
            array_k_K.append(password)
            
        elif re.search('l|L', password[0]):
            array_l_L.append(password)
            
        elif re.search('m|M', password[0]):
            array_m_M.append(password)
            
        elif re.search('n|N', password[0]): 
            array_n_N.append(password)
            
        elif re.search('o|O', password[0]):
            array_o_O.append(password)
            
        elif re.search('p|P', password[0]): 
            array_p_P.append(password)
            
        elif re.search('q|Q', password[0]):
            array_q_Q.append(password)
            
        elif re.search('r|R', password[0]): 
            array_r_R.append(password)
            
        elif re.search('s|S', password[0]):
            array_s_S.append(password)
            
        elif re.search('t|T', password[0]): 
            array_t_T.append(password)
            
        elif re.search('u|U', password[0]):
            array_u_U.append(password)
            
        elif re.search('v|V', password[0]): 
            array_v_V.append(password)
            
        elif re.search('w|W', password[0]):
            array_w_W.append(password)
            
        elif re.search('x|X', password[0]): 
            array_x_X.append(password)
            
        elif re.search('y|Y', password[0]):
            array_y_Y.append(password)
            
        elif re.search('z|Z', password[0]): 
            array_z_Z.append(password)
        
        else:
            array_symbol.append(password)
        
    i = i + 1
    
pswd_try = pd.read_csv("0_copy.txt", sep = ":",
                       header = None, error_bad_lines = False,
                       encoding="ISO-8859-1", engine = 'python'
                       )    

i = 0
array_0_try = []
array_1_try = []
array_2_try = []
array_3_try = []
array_4_try = []
array_5_try = []
array_6_try = []
array_7_try = []
array_8_try = []
array_9_try = []

array_a_A_try = []
array_b_B_try = []
array_c_C_try = []
array_d_D_try = []
array_e_E_try = []
array_f_F_try = []
array_g_G_try = []
array_h_H_try = []
array_i_I_try = []
array_j_J_try = []
array_k_K_try = []
array_l_L_try = []
array_m_M_try = []
array_n_N_try = []
array_o_O_try = []
array_p_P_try = []
array_q_Q_try = []
array_r_R_try = []
array_s_S_try = []
array_t_T_try = []
array_u_U_try = []
array_v_V_try = []
array_w_W_try = []
array_x_X_try = []
array_y_Y_try = []
array_z_Z_try = []

array_symbol_try = []

length_pswd_try = len(pswd_try)

while(i < length_pswd_try):
    password_try = pswd.iloc[i, 1]
    password_try = str(password_try)
    if password_try != 'None' and password_try != 'nan':
        
        #array.append(password)
        
        if re.search('0', password_try[0]):
            array_0_try.append(password_try)
            
        elif re.search('1', password_try[0]):
            array_1_try.append(password_try)
            
        elif re.search('2', password_try[0]): 
            array_2_try.append(password_try)
            
        elif re.search('3', password_try[0]):
            array_3_try.append(password_try)
            
        elif re.search('4', password_try[0]): 
            array_4_try.append(password_try)
            
        elif re.search('5', password_try[0]):
            array_5_try.append(password_try)
            
        elif re.search('6', password_try[0]): 
            array_6_try.append(password_try)
            
        elif re.search('7', password_try[0]):
            array_7_try.append(password_try)
            
        elif re.search('8', password_try[0]): 
            array_8_try.append(password_try)
            
        elif re.search('9', password_try[0]):
            array_9_try.append(password_try)
            
        elif re.search('a|A', password_try[0]):
            array_a_A_try.append(password_try)
            
        elif re.search('b|B', password_try[0]): 
            array_b_B_try.append(password_try)
            
        elif re.search('c|C', password_try[0]):
            array_c_C_try.append(password_try)
            
        elif re.search('d|D', password[0]): 
            array_d_D_try.append(password)
            
        elif re.search('e|E', password[0]):
            array_e_E_try.append(password)
            
        elif re.search('f|F', password[0]): 
            array_f_F_try.append(password)
            
        elif re.search('g|G', password[0]):
            array_g_G_try.append(password)
            
        elif re.search('h|H', password[0]): 
            array_h_H_try.append(password)
            
        elif re.search('i|I', password[0]):
            array_i_I_try.append(password)
            
        elif re.search('j|J', password[0]):
            array_j_J_try.append(password)
            
        elif re.search('k|K', password[0]): 
            array_k_K_try.append(password)
            
        elif re.search('l|L', password[0]):
            array_l_L_try.append(password)
            
        elif re.search('m|M', password[0]):
            array_m_M_try.append(password)
            
        elif re.search('n|N', password[0]): 
            array_n_N_try.append(password)
            
        elif re.search('o|O', password[0]):
            array_o_O_try.append(password)
            
        elif re.search('p|P', password[0]): 
            array_p_P_try.append(password)
            
        elif re.search('q|Q', password[0]):
            array_q_Q_try.append(password)
            
        elif re.search('r|R', password[0]): 
            array_r_R_try.append(password)
            
        elif re.search('s|S', password[0]):
            array_s_S_try.append(password)
            
        elif re.search('t|T', password[0]): 
            array_t_T_try.append(password)
            
        elif re.search('u|U', password[0]):
            array_u_U_try.append(password)
            
        elif re.search('v|V', password[0]): 
            array_v_V_try.append(password)
            
        elif re.search('w|W', password[0]):
            array_w_W_try.append(password)
            
        elif re.search('x|X', password[0]): 
            array_x_X_try.append(password)
            
        elif re.search('y|Y', password[0]):
            array_y_Y_try.append(password)
            
        elif re.search('z|Z', password[0]): 
            array_z_Z_try.append(password)
        
        else:
            array_symbol_try.append(password)
        
    i = i + 1

length_pswd = len(pswd) 

len_array_0 = len(array_0)
len_array_1 = len(array_1)
len_array_2 = len(array_2)
len_array_3 = len(array_3)
len_array_4 = len(array_4)
len_array_5 = len(array_5)
len_array_6 = len(array_6)
len_array_7 = len(array_7)
len_array_8 = len(array_8)
len_array_9 = len(array_9)

len_array_a_A = len(array_a_A)
len_array_b_B = len(array_b_B)
len_array_c_C = len(array_c_C)
len_array_d_D = len(array_d_D)
len_array_e_E = len(array_e_E)
len_array_f_F = len(array_f_F)
len_array_g_G = len(array_g_G)
len_array_h_H = len(array_h_H)
len_array_i_I = len(array_i_I)
len_array_j_J = len(array_j_J)
len_array_k_K = len(array_k_K)
len_array_l_L = len(array_l_L)
len_array_m_M = len(array_m_M)
len_array_n_N = len(array_n_N)
len_array_o_O = len(array_o_O)
len_array_p_P = len(array_p_P)
len_array_q_Q = len(array_q_Q)
len_array_r_R = len(array_r_R)
len_array_s_S = len(array_s_S)
len_array_t_T = len(array_t_T)
len_array_u_U = len(array_u_U)
len_array_v_V = len(array_v_V)
len_array_w_W = len(array_w_W)
len_array_x_X = len(array_x_X)
len_array_y_Y = len(array_y_Y)
len_array_z_Z = len(array_z_Z)
len_array_symbol = len(array_symbol)

length_pswd_try = len(pswd_try) 

len_array_0_try = len(array_0_try)
len_array_1_try = len(array_1_try)
len_array_2_try = len(array_2_try)
len_array_3_try = len(array_3_try)
len_array_4_try = len(array_4_try)
len_array_5_try = len(array_5_try)
len_array_6_try = len(array_6_try)
len_array_7_try = len(array_7_try)
len_array_8_try = len(array_8_try)
len_array_9_try = len(array_9_try)

len_array_a_A_try = len(array_a_A_try)
len_array_b_B_try = len(array_b_B_try)
len_array_c_C_try = len(array_c_C_try)
len_array_d_D_try = len(array_d_D_try)
len_array_e_E_try = len(array_e_E_try)
len_array_f_F_try = len(array_f_F_try)
len_array_g_G_try = len(array_g_G_try)
len_array_h_H_try = len(array_h_H_try)
len_array_i_I_try = len(array_i_I_try)
len_array_j_J_try = len(array_j_J_try)
len_array_k_K_try = len(array_k_K_try)
len_array_l_L_try = len(array_l_L_try)
len_array_m_M_try = len(array_m_M_try)
len_array_n_N_try = len(array_n_N_try)
len_array_o_O_try = len(array_o_O_try)
len_array_p_P_try = len(array_p_P_try)
len_array_q_Q_try = len(array_q_Q_try)
len_array_r_R_try = len(array_r_R_try)
len_array_s_S_try = len(array_s_S_try)
len_array_t_T_try = len(array_t_T_try)
len_array_u_U_try = len(array_u_U_try)
len_array_v_V_try = len(array_v_V_try)
len_array_w_W_try = len(array_w_W_try)
len_array_x_X_try = len(array_x_X_try)
len_array_y_Y_try = len(array_y_Y_try)
len_array_z_Z_try = len(array_z_Z_try)
len_array_symbol_try = len(array_symbol_try)   

match = [] 
# start to find the matched passwords
i = 0
j = 0 

while( i < len_array_0_try ):
    if array_0_try[i] != 'None' and array_0_try[i] != 'nan':

        while(j < len_array_0):
        
            if array_0[j] != 'None' and array_0[j] != 'nan':
                        
                        if(array_0_try[i] == array_0[j]):
                            print("array_0_try[i], i, array_0[j], j",
                                  array_0_try[i], i, array_0[j], j)
                            match.append(array_0_try[i])
                            #print(password)
                            print("match")
            j = j + 1

    j = 0    
    i = i + 1
 
                       
i = 0
j = 0 
while( i < len_array_1_try ):

    if array_1_try[i] != 'None' and array_1_try[i] != 'nan':
        
        while(j < len_array_1):
        
            if array_1[j] != 'None' and array_1[j] != 'nan':
                        
                        if(array_1_try[i] == array_1[j]):
                            print("array_1_try[i], i, array_1[j], j",
                                  array_1_try[i], i, array_1[j], j)
                            match.append(array_1_try[i])
                            #print(password)
                            print("match")
            j = j + 1 
    j = 0    
    i = i + 1    

i = 0
j = 0 
while( i < len_array_2_try ):

    if array_2_try[i] != 'None' and array_2_try[i] != 'nan':
        
        while(j < len_array_2):
        
            if array_2[j] != 'None' and array_2[j] != 'nan':
                        
                        if(array_2_try[i] == array_2[j]):
                            print("array_2_try[i], i, array_2[j], j",
                                  array_2_try[i], i, array_2[j], j)
                            match.append(array_2_try[i])
                            #print(password)
                            print("match")
            j = j + 1 
    j = 0    
    i = i + 1                    
                        
                        
                        
'''                        

        elif re.search('1', password2[0]):
            
            while(j < len_array_1):
                        
                        if(password2 == array_1[j]):
                            print("password2, array_1[j], j",
                                  password2, array_1[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1

        elif re.search('2', password2[0]):
            
            while(j < len_array_2):
                        
                        if(password2 == array_2[j]):
                            print("password2, array_2[j], j",
                                  password2, array_2[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1

        elif re.search('3', password2[0]):
            
            while(j < len_array_3):
                        
                        if(password2 == array_3[j]):
                            print("password2, array_3[j], j",
                                  password2, array_3[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1    
                        
        elif re.search('4', password2[0]):
            
            while(j < len_array_4):
                        
                        if(password2 == array_4[j]):
                            print("password2, array_4[j], j",
                                  password2, array_4[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1
    
        elif re.search('5', password2[0]):
            
            while(j < len_array_5):
                        
                        if(password2 == array_5[j]):
                            print("password2, array_5[j], j",
                                  password2, array_5[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1
                        
        elif re.search('6', password2[0]):
            
            while(j < len_array_6):
                        
                        if(password2 == array_6[j]):
                            print("password2, array_6[j], j",
                                  password2, array_6[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1                        
                        
                        
        elif re.search('7', password2[0]):
            
            while(j < len_array_7):
                        
                        if(password2 == array_7[j]):
                            print("password2, array_7[j], j",
                                  password2, array_7[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1




        elif re.search('8', password2[0]):
            
            while(j < len_array_8):
                        
                        if(password2 == array_8[j]):
                            print("password2, array_8[j], j",
                                  password2, array_8[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1                        
                        
                        
                        
                        
        elif re.search('9', password2[0]):
            
            while(j < len_array_9):
                        
                        if(password2 == array_9[j]):
                            print("password2, array_9[j], j",
                                  password2, array_9[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1                        
                        
                        
        elif re.search('a|A', password2[0]):
            
            while(j < len_array_a_A):
                        
                        if(password2 == array_a_A[j]):
                            print("password2, array_a_A[j], j",
                                  password2, array_a_A[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1
                        
                        
                        
        elif re.search('b|B', password2[0]):
            
            while(j < len_array_b_B):
                        
                        if(password2 == array_b_B[j]):
                            print("password2, array_b_B[j], j",
                                  password2, array_b_B[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1





        elif re.search('c|C', password2[0]):
            
            while(j < len_array_c_C):
                        
                        if(password2 == array_c_C[j]):
                            print("password2, array_c_C[j], j",
                                  password2, array_c_C[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1



        elif re.search('d|D', password2[0]):
            
            while(j < len_array_d_D):
                        
                        if(password2 == array_d_D[j]):
                            print("password2, array_d_D[j], j",
                                  password2, array_d_D[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1

        elif re.search('e|E', password2[0]):
            
            while(j < len_array_e_E):
                        
                        if(password2 == array_e_E[j]):
                            print("password2, array_e_E[j], j",
                                  password2, array_e_E[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1


        elif re.search('f|F', password2[0]):
            
            while(j < len_array_f_F):
                        
                        if(password2 == array_f_F[j]):
                            print("password2, array_f_F[j], j",
                                  password2, array_f_F[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1


        elif re.search('g|G', password2[0]):
            
            while(j < len_array_g_G):
                        
                        if(password2 == array_g_G[j]):
                            print("password2, array_g_G[j], j",
                                  password2, array_g_G[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1


        elif re.search('h|H', password2[0]):
            
            while(j < len_array_h_H):
                        
                        if(password2 == array_h_H[j]):
                            print("password2, array_h_H[j], j",
                                  password2, array_h_H[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1


        elif re.search('i|I', password2[0]):
            
            while(j < len_array_i_I):
                        
                        if(password2 == array_i_I[j]):
                            print("password2, array_i_I[j], j",
                                  password2, array_i_I[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1

        elif re.search('j|J', password2[0]):
            
            while(j < len_array_j_J):
                        
                        if(password2 == array_j_J[j]):
                            print("password2, array_j_J[j], j",
                                  password2, array_j_J[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1

        elif re.search('k|K', password2[0]):
            
            while(j < len_array_k_K):
                        
                        if(password2 == array_k_K[j]):
                            print("password2, array_k_K[j], j",
                                  password2, array_k_K[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1

        elif re.search('l|L', password2[0]):
            
            while(j < len_array_l_L):
                        
                        if(password2 == array_l_L[j]):
                            print("password2, array_l_L[j], j",
                                  password2, array_l_L[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1


        elif re.search('m|M', password2[0]):
            
            while(j < len_array_m_M):
                        
                        if(password2 == array_m_M[j]):
                            print("password2, array_m_M[j], j",
                                  password2, array_m_M[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1


        elif re.search('n|N', password2[0]):
            
            while(j < len_array_n_N):
                        
                        if(password2 == array_n_N[j]):
                            print("password2, array_n_N[j], j",
                                  password2, array_n_N[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1


        elif re.search('o|O', password2[0]):
            
            while(j < len_array_o_O):
                        
                        if(password2 == array_o_O[j]):
                            print("password2, array_o_O[j], j",
                                  password2, array_o_O[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1



        elif re.search('p|P', password2[0]):
            
            while(j < len_array_p_P):
                        
                        if(password2 == array_p_P[j]):
                            print("password2, array_p_P[j], j",
                                  password2, array_p_P[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1



        elif re.search('q|Q', password2[0]):
            
            while(j < len_array_q_Q):
                        
                        if(password2 == array_q_Q[j]):
                            print("password2, array_q_Q[j], j",
                                  password2, array_q_Q[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1



        elif re.search('r|R', password2[0]):
            
            while(j < len_array_r_R):
                        
                        if(password2 == array_r_R[j]):
                            print("password2, array_r_R[j], j",
                                  password2, array_r_R[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1


        elif re.search('s|S', password2[0]):
            
            while(j < len_array_s_S):
                        
                        if(password2 == array_s_S[j]):
                            print("password2, array_s_S[j], j",
                                  password2, array_s_S[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1


        elif re.search('t|T', password2[0]):
            
            while(j < len_array_t_T):
                        
                        if(password2 == array_t_T[j]):
                            print("password2, array_t_T[j], j",
                                  password2, array_t_T[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1



        elif re.search('u|U', password2[0]):
            
            while(j < len_array_u_U):
                        
                        if(password2 == array_u_U[j]):
                            print("password2, array_u_U[j], j",
                                  password2, array_u_U[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1


        elif re.search('v|V', password2[0]):
            
            while(j < len_array_v_V):
                        
                        if(password2 == array_v_V[j]):
                            print("password2, array_v_V[j], j",
                                  password2, array_v_V[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1


        elif re.search('w|W', password2[0]):
            
            while(j < len_array_w_W):
                        
                        if(password2 == array_w_W[j]):
                            print("password2, array_w_W[j], j",
                                  password2, array_w_W[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1


        elif re.search('x|X', password2[0]):
            
            while(j < len_array_x_X):
                        
                        if(password2 == array_x_X[j]):
                            print("password2, array_x_X[j], j",
                                  password2, array_x_X[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1


        elif re.search('y|Y', password2[0]):
            
            while(j < len_array_y_Y):
                        
                        if(password2 == array_y_Y[j]):
                            print("password2, array_y_Y[j], j",
                                  password2, array_y_Y[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1


        elif re.search('z|Z', password2[0]):
            
            while(j < len_array_z_Z):
                        
                        if(password2 == array_z_Z[j]):
                            print("password2, array_z_Z[j], j",
                                  password2, array_z_Z[j], j)
                            match.append(password2)
                            #print(password)
                            print("match")
                        j = j + 1
                        
        else:         
                    
                    while(j < len_array_symbol):

                        
                        if(password2 == array_symbol[j]):
                            print("password2, array_symbol[j], j",
                                  password2, array_symbol[j], j)
                            match.append(password2)
                            #print(password)
                            print("match3")
                        j = j + 1
   
    #print("i", i)                
    i = i + 1
'''    
match = sorted(match, key=str.lower)
length_match = len(match)  
print("Length: ",length_match, "Match: ", match)
np.savetxt('match.csv',(match), fmt='%s')


 
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        