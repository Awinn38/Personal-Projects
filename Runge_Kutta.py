import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def Runge_Kutta(x0, y0, z0, sigma = 10.0, rho = 28.0, beta = (8.0/3.0), n_steps = 50000, dt = .005):
   
    x = np.zeros(n_steps)
    y = np.zeros(n_steps)
    z = np.zeros(n_steps)
    t = np.zeros(n_steps)
    
    #initial Conditions
    x[0] = x0
    y[0] = y0
    z[0] = z0
    
    i = 1
    
    
    while i < n_steps:
        t[i] = dt * i
        
        kx_1 = sigma * (y[i-1] - x[i-1])
        ky_1 = rho * x[i-1] - x[i-1] * z[i-1] - y[i-1]
        kz_1 = x[i-1] * y[i-1] - beta * z[i-1]
        x1 = x[i] + 0.5 * dt * kx_1
        y1 = y[i] + 0.5 * dt * ky_1
        z1 = z[i] + 0.5 * dt * kz_1
        
        kx_2 = sigma * (y1 - x1)
        ky_2 = rho * x1 - x1 * z1 - y1
        kz_2 = x1 * y1 - beta * z1
        x2 = x[i] + 0.5 * dt * kx_2
        y2 = y[i] + 0.5 * dt * ky_2
        z2 = z[i] + 0.5 * dt * kz_2
        
        kx_3 = sigma * (y2 - x2)
        ky_3 = rho * x2 - x2 * z2 - y2
        kz_3 = x2 * y2 - beta * z2
        x3 = x2 + 0.5 * dt * kx_3
        y3 = y2 + 0.5 * dt * ky_3
        z3 = z2 + 0.5 * dt * kz_3
        
        kx_4 = sigma * (y3 - x3)
        ky_4 = rho * x3 - x3 * z3 - y3
        kz_4 = x3 * y3 - beta * z3

        
        x[i] = x[i-1] + (dt/6) * (kx_1 + 2*kx_2 + 2 * kx_3 + kx_4)
        y[i] = y[i-1] + (dt/6) * (ky_1 + 2*ky_2 + 2 * ky_3 + ky_4)
        z[i] = z[i-1] + (dt/6) * (kz_1 + 2*kz_2 + 2 * kz_3 + kz_4)
        i+=1
        
    fig = plt.figure()
    ax = fig.add_subplot(111, projection ='3d')
    
    ax.plot(x,y,z)
    fig.show()
    return x,y,z,t
xa,ya,za,ta = Runge_Kutta(1.0,1.0,1.0)

xb,yb,zb,tb = Runge_Kutta(1.0,1.0,1.001)

rms = np.sqrt(((xa-xb)**2 + (ya-yb)**2 + (za-zb)**2)/3)
plt.figure()
plt.plot(ta,(np.log(rms)))
plt.xlabel("time")
plt.ylabel("log[rms]")
plt.show()


#since this is not possible to do with discrete values, i just approximated the slope of the log plot of x_perturbed-x and then calculated at what time the value is equal to e
def eFolding(xa,xb):
    exp_start = 1
    exp_end = 90
    rms = np.log(np.abs(xb-xa))
    x_start = float(rms[exp_start])
    x_end = float(rms[exp_end])
    #print(x_start, "  ",x_end)
    dxdt = (x_end-x_start) / (exp_end -1)
    
    
    eft = np.e / dxdt
    print("The E Folding time is: ",eft)
    return eft
    
# Theoretically, since the lyaponov exponent can be written as e = e^lt, the expononent is simply the inverse of the e-folding time
def Lyaponov(e_folding_time):
    t = e_folding_time
    le = 1 /t
    print("The Lyaponov Exponent is: ",le)
        
        
eft = eFolding(xa,xb)
Lyaponov(eft)        

#   a(0,1.0,20.0)