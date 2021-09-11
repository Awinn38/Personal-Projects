# using Plots
# pyplot()
# plot(rand(4,4))

# import Pkg; Pkg.add("DifferentialEquations")
# using DifferentialEquations
# f(u,p,t) = 1.01*u
# u0 = 1/2
# tspan = (0.0,1.0)
# prob = ODEProblem(f,u0,tspan)
# sol = solve(prob,Tsit5())

# Pkg.add("Optim")
# using Optim
# rosenbrock(x) =  (1.0 - x[1])^2 + 100.0 * (x[2] - x[1]^2)^2
# result = optimize(rosenbrock, zeros(2), BFGS())

# x = symbols("x")
# SymPy.simplify(sin(x)^2 + cos(x)^2)	
# SymPy.factor(x^2 + 2x+ 1)

# using CalculusWithJulia
# using Plots
# plotly()

# position(t) = 60*t
# plot(position,0,3)
