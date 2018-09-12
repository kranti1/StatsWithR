from sympy import Symbol, Derivative
import math
x= Symbol('x n y')

function= ((54*x) / math.log*x)-106

deriv= Derivative(function, x)
print(deriv.doit().subs({x:8}))
