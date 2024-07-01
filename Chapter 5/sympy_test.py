"""
fractions : 유리수 계산

x*(2/5) = 1760
"""

from fractions import Fraction
import sympy

x = sympy.symbols("x")

f = sympy.Eq(x*Fraction('2/5'),1760)
result = sympy.solve(f)

print(result)
print(type(result)) #list

remains = result[0] - 1760
print(remains)