import numpy as np
import ConstantsWilsonTemp
import SatLiquRacket
import experimentalEqns
import scipy.optimize as optimize


def Minimization(opt):
    Vl1, Vl2 = SatLiquRacket.SatLiqVolumeRacket(
        ConstantsWilsonTemp.Vl1_WilsonTemp, ConstantsWilsonTemp.Vl2_WilsonTemp, ConstantsWilsonTemp.Zc1, ConstantsWilsonTemp.Zc2, ConstantsWilsonTemp.Tr1, ConstantsWilsonTemp.Tr2)
    GEE = experimentalEqns.Experamental_GRT(
        ConstantsWilsonTemp.x1_WilsonTemp[1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.x2_WilsonTemp [1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.GammaE1_WilsonTemp[1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.GammaE2_WilsonTemp[1:ConstantsWilsonTemp.end-1])
    return (np.sum((((-ConstantsWilsonTemp.x1_WilsonTemp[1:ConstantsWilsonTemp.end-1] * (np.log(ConstantsWilsonTemp.x1_WilsonTemp[1:ConstantsWilsonTemp.end-1]
                                                    + ((Vl2/Vl1) * np.exp(-opt[0]/(ConstantsWilsonTemp.R*ConstantsWilsonTemp.T_WilsonTemp))) * ConstantsWilsonTemp.x2_WilsonTemp [1:ConstantsWilsonTemp.end-1])))
                     - (ConstantsWilsonTemp.x2_WilsonTemp [1:ConstantsWilsonTemp.end-1] * (np.log(ConstantsWilsonTemp.x2_WilsonTemp [1:ConstantsWilsonTemp.end-1]
                                                     + ((Vl1/Vl2) * np.exp(-opt[1]/(ConstantsWilsonTemp.R*ConstantsWilsonTemp.T_WilsonTemp))) * ConstantsWilsonTemp.x1_WilsonTemp[1:ConstantsWilsonTemp.end-1]))))
                    - GEE[1:ConstantsWilsonTemp.end-1]) / (GEE[1:ConstantsWilsonTemp.end-1])) ** 2) / (len(ConstantsWilsonTemp.P_WilsonTemp)-2)


result = optimize.minimize(Minimization, ConstantsWilsonTemp.xguess,
                           method='nelder-mead', options={'xatol': 1e-8, 'disp': False})


def optimize_Results():
    return result.x
