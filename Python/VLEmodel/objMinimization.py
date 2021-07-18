import numpy as np
import Constants
import SatLiquRacket
import experimentalEqns
import scipy.optimize as optimize


def Minimization(opt):
    Vl1, Vl2 = SatLiquRacket.SatLiqVolumeRacket(
        Constants.Vl1, Constants.Vl2, Constants.Zc1, Constants.Zc2, Constants.Tr1, Constants.Tr2)
    GEE = experimentalEqns.Experamental_GRT(
        Constants.x1[1:11], Constants.x2[1:11], Constants.GammaE1[1:11], Constants.GammaE2[1:11])
    return (np.sum((((-Constants.x1[1:11] * (np.log(Constants.x1[1:11]
                                                    + ((Vl2/Vl1) * np.exp(-opt[0]/(Constants.R*Constants.T))) * Constants.x2[1:11])))
                     - (Constants.x2[1:11] * (np.log(Constants.x2[1:11]
                                                     + ((Vl1/Vl2) * np.exp(-opt[1]/(Constants.R*Constants.T))) * Constants.x1[1:11]))))
                    - GEE[1:11]) / (GEE[1:11])) ** 2) / (len(Constants.P)-2)


result = optimize.minimize(Minimization, Constants.xguess,
                           method='nelder-mead', options={'xatol': 1e-8, 'disp': False})


def optimize_Results():
    return result.x
