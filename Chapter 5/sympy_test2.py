"""
x^2 = 1
"""
import sympy

x = sympy.symbols("x")

f = sympy.Eq(x**2, 1)
results = sympy.solve(f)


print(type(results)) # list
print(results)


