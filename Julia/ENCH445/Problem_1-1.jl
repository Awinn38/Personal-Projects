# x,y = symbols("x,y")
# Eqn_1 = 2*x*y - 2*x^)2 + 4*sin(y) + 4
# Eqn_2 = 3*x^2 - 2*x*y^2 + 5*cos(x) + 4
# convert(AbstractFloat,Eqn_1(1,1))
function mysqrt(x)
    x < 0 && throw(DomainError("x is negative"))
    x^0.5
end
mysqrt(1)
