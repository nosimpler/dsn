#!usr/bin/python
import sympy as sp
from sympy import *
import numpy as np
# returns column unit vectors corresponding to a partition

def partition_to_units(partition):    
    flatten = lambda l: [item for sublist in l for item in sublist]
    n_cols = len(partition)
    n_rows = len(flatten(partition))
    vec = np.zeros((n_rows, n_cols))
    for i,p in enumerate(partition):
        vec[p,i] = 1 
    return sp.Matrix(vec.astype(int))

def partition_to_nulls(partition):
    u = partition_to_units(partition)
    return u.T.nullspace()

def symmetrize_jacobian(J):
    J_sym = (J + J.T)/2
    return J_sym

def reduce_jacobian(colvecs, J):
    new_J = colvecs.T*J*colvecs
    return new_J

def gershgorin_disc(J):
    sz = J.shape[0]
    new_J = sp.zeros(sz, sz)
    for i in range(sz):
        for j in range(sz):
            if i != j:
                new_J[i,j] = abs(J[i,j])
            else:
                new_J[i,i] = J[i,i]
    return sp.ones(1, sz)*new_J
    

if __name__ == '__main__':
    partition = [[0,1],[2,3]]
    u = partition_to_units(partition)
    n = partition_to_nulls(partition)
    vars = Matrix(["v_1", "v_2", "u_1", "u_2"])
    params = ["w_1", "w_2", "a_1", "a_2", "b_1", "b_2", 'tau_1', 'tau_2']
    ODE_sys = Matrix(["v_1-(v_1**3)/3 - u_1 + w_1*v_2",
                "v_2-(v_2**3)/3 - u_2 + w_2*v_1",
                "a_1*(b_1*v_1 - u_1)",
                "a_2*(b_2*v_2 - u_2)"])
    J = ODE_sys.jacobian(vars)
    J_sym = symmetrize_jacobian(J)
    J_reduced = reduce_jacobian(u,J)
    print(J_reduced.shape[1])
print(gershgorin_disc(J_reduced))
