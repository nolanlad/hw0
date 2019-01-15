from sympy import *
import numpy as np

endl = "\n"

def np_to_latex(A):
    s = "\\begin{bmatrix}"
    for i in A:
        for j in i:
            s+=(latex(j) + "&")
        s+="\\\\[0.3em]\n"
    s+="\\end{bmatrix}\n"
    return s

def equatify(x):
    return "\\[\n" + str(x) + "\\]\n"

lam = symbols("\\lambda")
A = [[0, 1],[-3,2]]

eig_A = [[0 - lam, 1],[-3,2-lam]]

deter = (eig_A[0][0]*eig_A[1][1] - eig_A[0][1]*eig_A[1][0])

text = equatify(" A = " + np_to_latex(A)) + equatify("det"+np_to_latex(eig_A))
text+="\n"
text+=equatify(latex(deter))+"\n"
text+=equatify(latex(lam) + " = " + latex(solve(deter)) + "\n" )

print(text)

text2 = ""

b,m,g,l, thet, k,r =  symbols("b m g l \\theta k r")

text2+= equatify("\\tau _g = "+latex(-m*g*l*sin(thet)))
text2+=endl
text2+= equatify("\\tau_s = "+latex(-k*((2*l)/3)*((2*l)/3)*sin(thet)*cos(thet)))

text2+= equatify("\\tau _g = "+latex(-m*g*l*sin(thet)))

text2+= equatify("ml^2 \\ddot \\theta  = -b \\dot \\theta "+latex(-m*g*l*thet)+latex(-k*((2*l)/3)*((2*l)/3)*thet))

eqn = m*l*l*r*r + b * r + (m*g*l + (k*((2*l)/3)*((2*l)/3)))

text2+= equatify(latex(eqn))
text2+=  equatify(latex(solve(eqn,r)))
print(text2)
