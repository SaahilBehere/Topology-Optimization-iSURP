# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 21:08:08 2021

@author: saahi
"""

import numpy as np
import matplotlib.pyplot as plt

##params 

# endpoints
a = 0
b = np.pi
#boundary conditions
ua = 0
ub = 0
#number of points
n = 2
dx = (b-a)/(n+1)
# Setting up K,F
def FEM(n,dx,a,b,ua,ub):
    K = np.eye(n)
    i,j = np.indices(K.shape)
    
    K[i==j] = 2
    K[i==j+1] = -1
    K[i==j-1] = -1
    K *= 1/dx
    
    # Function 
    f = lambda x: np.sin(x)
    
    # Mf = F
    M = np.eye(n)
    
    M[i==j] = 2/3
    M[i==j+1] = 1/6
    M[i==j-1] = 1/6
    M *= dx
    
    x_i = np.linspace(a,b,n+2)
    
    f_x = f(x_i)
    
    F = M@f_x[1:-1]
    F[0] += f_x[0]*dx/6 - (-ua/dx) 
    F[-1] += f_x[-1]*dx/6 - (-ub/dx)
    
    # F[0] = (f(x_1))*2h/3 + (f(x_2))*h/6. F_1 = f(0)*h/6 + F[0];
    # KU[0] = (u(x_1))*2/h + (u(x_2))*(-1/h); KU_1 = KU[0] + (u_a)*(-h/6)
    #Transfer (u_a)*(-h/6) to RHS so that U can be calculated
    # RHS[0] = F_1 - (u_a)*(-h/6)
    #Similarly for last term
    
    # KU = F
    
    U = np.matmul(np.linalg.inv(K),F)
    U = np.insert(U,[0,n],[ua,ub])
    return U

k_array = [2,4,10,20]  #Numerous k values for checking 

for k in k_array:
    x_i = np.linspace(a,b,k+2)
    dx = (b-a)/(k+1)
    U =  FEM(k,dx,a,b,ua,ub)
    plt.plot(x_i,U)

plt.legend()
