from scipy.optimize import fsolve   # numerical solver
from scipy.integrate import quad    # integration
import numpy as np
import matplotlib.pyplot as plt     # plotting
from trigonometric_shortcuts import *
import sympy as sym
sym.init_printing()


def print_mat(mat):
    for i in mat:
        print(i, sep="\n")


a = sym.Symbol('α')
r = sym.Symbol('Γ')

a_val = sym.pi/4
r_val = sym.pi/2
pol_val = None
J = sym.Matrix([[0], [1]])  # non-polarized light beam


mat1 = sym.Matrix([[sym.cos(a), -sym.sin(a)], [sym.sin(a), sym.cos(a)]])
mat2 = sym.Matrix([[1, 0],[0, sym.exp(-sym.I * r)]])
mat3 = sym.Matrix([[sym.cos(a), sym.sin(a)], [-sym.sin(a), sym.cos(a)]])
polarizer = sym.Matrix([[1, 0], [0, 1]]) # no polarizer

if pol_val is not None: # this is output polarization, not input. Input polarization is controlled through J
    if pol_val == 'x':
        polarizer = sym.Matrix([[1, 0], [0, 0]]) # x polarizer
    elif pol_val == 'y':
        polarizer = sym.Matrix([[0, 0], [0, 1]]) # y polarizer
    else:
        polarizer = sym.Matrix(pol_val)  # arbitrary polarizer

Mj = polarizer * mat1 * mat2 * mat3
if a_val is not None:
    Mj = Mj.subs([(a, a_val)])
if r_val is not None:
    Mj = Mj.subs([(r, r_val)])

MjJ = Mj * J

print("Resulting Mj Matrix Shape:", Mj.shape)
g_Mj = sym.gcd(tuple(Mj))
gMj = sym.MatMul(g_Mj, Mj/g_Mj, evaluate=False)
sym.pprint(sym.simplify(gMj))
print(sym.simplify(Mj))
print("")

print("Resulting J' = Mj * J Matrix Shape:", MjJ.shape)
g_MjJ = sym.gcd(tuple(MjJ))
gMjJ = sym.MatMul(g_MjJ, MjJ/g_MjJ, evaluate=False)
sym.pprint(sym.simplify(gMjJ))
print(sym.simplify(MjJ))
