"""
연립 방정식 구하기
x+y = 10
x-y = 4
"""
import sympy

x, y = sympy.symbols('x y')

f1 = sympy.Eq(x+y, 10)
f2 = sympy.Eq(x-y, 4)

results = sympy.solve([f1,f2]) #solve 안에 넣는 형태 주의!
print(type(results)) #dictionary

print(results)