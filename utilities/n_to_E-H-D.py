from scipy.optimize import fsolve   # numerical solver
from scipy.integrate import quad    # integration
import numpy as np
import matplotlib.pyplot as plt     # plotting
from trigonometric_shortcuts import *

sx = 1/np.sqrt(3)
sy = 1/np.sqrt(3)
sz = 1/np.sqrt(3)
sxyz = [sx, sy, sz]

nx = 1.5
ny = 1.6
nz = 1.7
nxyz = [nx, ny, nz]

# always define positive
n1 = 1.6547
n2 = 1.5391
n = [n1, -n1, n2, -n2]


def main():
    print("--- n1 ---")
    Eox1 = sx / (n1 ** 2 - nx ** 2)  # times common factor
    Eoy1 = sy / (n1 ** 2 - ny ** 2)  # times common factor
    Eoz1 = sz / (n1 ** 2 - nz ** 2)  # times common factor

    Dox1 = nx ** 2 * Eox1  # times common factor
    Doy1 = ny ** 2 * Eoy1  # times common factor
    Doz1 = nz ** 2 * Eoz1  # times common factor

    Hox1 = + (sy * Eoz1 - sz * Eoy1)  # times common factor
    Hoy1 = - (sx * Eoz1 - sz * Eox1)  # times common factor
    Hoz1 = + (sx * Eoy1 - sy * Eox1)  # times common factor

    print("Eox1: %10.5g\tEoy1: %10.5g\tEoz1: %10.5g\t" % (Eox1, Eoy1, Eoz1))
    print("Dox1: %10.5g\tDoy1: %10.5g\tDoz1: %10.5g\t" % (Dox1, Doy1, Doz1))
    print("Hox1: %10.5g\tHoy1: %10.5g\tHoz1: %10.5g\t" % (Hox1, Hoy1, Hoz1))

    print("\n--- n2 ---")
    Eox2 = sx / (n2 ** 2 - nx ** 2)  # times common factor
    Eoy2 = sy / (n2 ** 2 - ny ** 2)  # times common factor
    Eoz2 = sz / (n2 ** 2 - nz ** 2)  # times common factor

    Dox2 = nx ** 2 * Eox2  # times common factor
    Doy2 = ny ** 2 * Eoy2  # times common factor
    Doz2 = nz ** 2 * Eoz2  # times common factor

    Hox2 = + (sy * Eoz2 - sz * Eoy2)  # times common factor
    Hoy2 = - (sx * Eoz2 - sz * Eox2)  # times common factor
    Hoz2 = + (sx * Eoy2 - sy * Eox2)  # times common factor

    print("Eox2: %10.5g\tEoy2: %10.5g\tEoz2: %10.5g\t" % (Eox2, Eoy2, Eoz2))
    print("Dox2: %10.5g\tDoy2: %10.5g\tDoz2: %10.5g\t" % (Dox2, Doy2, Doz2))
    print("Hox2: %10.5g\tHoy2: %10.5g\tHoz2: %10.5g\t" % (Hox2, Hoy2, Hoz2))

if __name__ == "__main__":
    main()