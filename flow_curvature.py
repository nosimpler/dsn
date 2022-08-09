# -*- coding: utf-8 -*-
"""
Computes the flow-curvature manifold for the system
In progress...

"""
from sympy import *


def ddt(rhs, k):
    t = symbols('t')
    return diff(rhs, t, k)

# TODO: substitute in time-derivatives from original ODE
def flow_curvature_matrix(lhs, rhs):
    fcm = rhs
    J = rhs.jacobian(lhs)
    for i in range(len(lhs)-1):
        fcm = Matrix.hstack(fcm, ddt(rhs,i+1))
    return fcm

# near fixed points only!
def flow_curvature_matrix_fixed(lhs, rhs):
    fcm = rhs
    J = rhs.jacobian(lhs)
    for i in range(len(lhs)-1):
        fcm = Matrix.hstack(fcm, (J**i)*rhs)
    return fcm
# near fixed points only!
def flow_curvature_manifold_fixed(lhs, rhs):
    return det(flow_curvature_matrix_fixed(lhs, rhs))

if __name__ == '__main__':

    lhs = Matrix(["v_1", "v_2", "u_1", "u_2"])
    params = ["w_1", "w_2", "a_1", "a_2", "b_1", "b_2", 'tau_1', 'tau_2']
    rhs = Matrix(["v_1(t)-(v_1(t)**3)/3 - u_1(t) + w_1*v_2(t)",
                "v_2(t)-(v_2(t)**3)/3 - u_2(t) + w_2*v_1(t)",
                "a_1*(b_1*v_1(t) - u_1(t))",
                "a_2*(b_2*v_2(t) - u_2(t))"])
    print(flow_curvature_matrix_fixed(lhs, rhs))
    print(flow_curvature_manifold_fixed(lhs, rhs))
    print(flow_curvature_matrix(lhs, rhs))
      