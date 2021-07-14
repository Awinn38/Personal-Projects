import numpy as np
import pandas as pd
import Constants
import SatLiquRacket
import scipy.optimize as optimize

def Minimization(opt):
    VlMeth , VlWate = SatLiquRacket.SatLiqVolumeRacket(Constants.Vl1,Constants.Vl2,Constants.Zc1,Constants.Zc2,Constants.Tr1,Constants.Tr2)
    return (np.sum((((-Constants.x1[1:11] * (np.log(Constants.x1[1:11] + ((VlWate/VlMeth ) * np.exp(-opt[0]/(Constants.R*Constants.T))) * Constants.x2[1:11]))) - (Constants.x2[1:11] * (np.log(Constants.x2[1:11]) + ((VlMeth/VlWate)*np.exp(-opt[1]/(Constants.R*Constants.T))) * Constants.x1[1:11]))) - Constants.GEE[1:11]) / (Constants.GEE[1:11])) **2) / (len(Constants.P[1:11])-2)
result = optimize.minimize(Minimization,Constants.xguess)
if result.success:
    fitted_params = result.x
    print(fitted_params)
else:
    raise ValueError(result.message) 

