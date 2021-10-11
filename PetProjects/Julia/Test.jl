### Plots ###
# using Plots
# pyplot()
# plot(rand(4,4))

### DifferentialEquations ###
# import Pkg; Pkg.add("DifferentialEquations")
# using DifferentialEquations
# f(u,p,t) = 1.01*u
# u0 = 1/2
# tspan = (0.0,1.0)
# prob = ODEProblem(f,u0,tspan)
# sol = solve(prob,Tsit5())

### Optim ###
# Pkg.add("Optim")
# using Optim
# rosenbrock(x) =  (1.0 - x[1])^2 + 100.0 * (x[2] - x[1]^2)^2
# result = optimize(rosenbrock, zeros(2), BFGS())

# x = symbols("x")
# SymPy.simplify(sin(x)^2 + cos(x)^2)	
# SymPy.factor(x^2 + 2x+ 1)

### CalculusWithJulia ###
# using CalculusWithJulia
# using Plots
# plotly()

# position(t) = 60*t
# plot(position,0,3)

### LaTeXStrings ###
# using LaTeXStrings
# L" 2.55e{-6} \ \ \frac{mol}{m^3} "


### PyCall ###
# using PyCall; using SymPy
# py"""
# import math
# from sympy.solvers import solve
# from sympy import Symbol
# x = Symbol('x')

# Z = (0.1)*(481.6) + (x)*(155.9) + (0.9-x)*(48.2)-138
# print(solve(Z,x))
# """