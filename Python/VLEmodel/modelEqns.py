import numpy as np
import Constants
import SatLiquRacket
import objMinimization


def Wilson_Constants():
    Wil_Constants = objMinimization.optimize_Results()
    VlMeth, VlWate = SatLiquRacket.SatLiqVolumeRacket(
        Constants.VlMeth, Constants.VlWate, Constants.Zc1, Constants.Zc2, Constants.Tr1, Constants.Tr2)
    Alph1 = (VlWate/VlMeth)*np.exp(-Wil_Constants[0]/(Constants.R*Constants.T))
    Alph2 = (VlMeth/VlWate)*np.exp(-Wil_Constants[1]/(Constants.R*Constants.T))
    return Alph1, Alph2


Alpha1, Alpha2 = Wilson_Constants()


def Wilson_GibbsEx():
    Constants.GEM_Wilson[1:11] = (-Constants.x1[1:11] *
                                  np.log(Constants.x1[1:11] + Alpha1 *
                                         Constants.x2[1:11]) - Constants.x2[1:11] *
                                         np.log(Constants.x2[1:11] + Alpha2 * Constants.x1[1:11]))
    return Constants.GEM_Wilson
Wilson_GibbsEx()