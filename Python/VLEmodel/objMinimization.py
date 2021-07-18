import numpy as np
import ConstantsWilson
import SatLiquRacket
import experimentalEqns
import scipy.optimize as optimize


def Minimization(opt):
    Vl1, Vl2 = SatLiquRacket.SatLiqVolumeRacket(
        ConstantsWilson.Vl1_Wilson, ConstantsWilson.Vl2_Wilson, ConstantsWilson.ZcMeth_Willson, ConstantsWilson.ZcWate_Willson, ConstantsWilson.Tr1, ConstantsWilson.Tr2)
    GEE = experimentalEqns.Experamental_GRT(
        ConstantsWilson.x1_Willson[1:ConstantsWilson.end-1], ConstantsWilson.x2_Willson [1:ConstantsWilson.end-1], ConstantsWilson.GammaE1_Willson[1:ConstantsWilson.end-1], ConstantsWilson.GammaE2_Willson[1:ConstantsWilson.end-1])
    return (np.sum((((-ConstantsWilson.x1_Willson[1:ConstantsWilson.end-1] * (np.log(ConstantsWilson.x1_Willson[1:ConstantsWilson.end-1]
                                                    + ((Vl2/Vl1) * np.exp(-opt[0]/(ConstantsWilson.R*ConstantsWilson.T_Willson))) * ConstantsWilson.x2_Willson [1:ConstantsWilson.end-1])))
                     - (ConstantsWilson.x2_Willson [1:ConstantsWilson.end-1] * (np.log(ConstantsWilson.x2_Willson [1:ConstantsWilson.end-1]
                                                     + ((Vl1/Vl2) * np.exp(-opt[1]/(ConstantsWilson.R*ConstantsWilson.T_Willson))) * ConstantsWilson.x1_Willson[1:ConstantsWilson.end-1]))))
                    - GEE[1:ConstantsWilson.end-1]) / (GEE[1:ConstantsWilson.end-1])) ** 2) / (len(ConstantsWilson.P_Willson)-2)


result = optimize.minimize(Minimization, ConstantsWilson.xguess,
                           method='nelder-mead', options={'xatol': 1e-8, 'disp': False})


def optimize_Results():
    return result.x
