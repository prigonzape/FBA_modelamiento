import numpy as np
from scipy.optimize import linprog
from numpy.linalg import solve

def miFuncion():
 import numpy as np
 from scipy.optimize import linprog
 from numpy.linalg import solve

 S = np.array([
 [1,0,-1,0,0,0,0,0],     #CO2
 [0,2,-2,-2,0,0,0,0],    #H2
 [0,0,-1,1,1,0,-1,0],    #F420
 [0,0,1,-1,1,0,0,0],     #I1
 [0,0,0,0,2,0,0,-2],     #H2O
 [0,0,0,1,-1,-1,0,0]])   #CH4
    
 b_eq = np.array([0,0,0,0,0,1])

 c = np.array([0,0,0,0,0,1,0,0])

 res = linprog(c, A_eq=S, b_eq=b_eq, bounds=(0, None))
 print('Optimal value:', res.fun, '\nX:', res.x)

if __name__ == "__main__":
    miFuncion()