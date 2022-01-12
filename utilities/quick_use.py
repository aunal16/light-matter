from scipy.optimize import fsolve   # numerical solver
from scipy.integrate import quad    # integration
import numpy as np
import matplotlib.pyplot as plt     # plotting
from trigonometric_shortcuts import *
import sympy as sym
sym.init_printing()

u = sym.Symbol('u')
Ec = sym.Symbol('Ec')
Efn = sym.Symbol('Efn')
kBT = sym.Symbol('kBT')

res = sym.integrate(sym.sqrt(u) / (sym.exp((u + Ec - Efn)/kBT) + 1), (u, 0, Efn-Ec))

sym.pprint(res)
