from gekko import GEKKO
m=GEKKO()
p=m.Param(1.2)
x=m.Array(m.Var,3)
eq0 = x[1]==x[0]+p
eq1 = x[2]-1==x[1]+x[0]
m.Equation(x[2]==x[1]**2)
m.Equations([eq0,eq1])
m.solve()
print(x[2].value)