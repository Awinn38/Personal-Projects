import numpy as np
import Constants
import SatLiquRacket
import objMinimization
import antoniesEqn


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


def Calculation_Gamma(x1, x2, alpha1, alpha2):
    GammaM1 = np.exp(-np.log(x1 + alpha1*x2) + x2*((alpha1 /
                                                    (x1 + alpha1*x2)) - (alpha2/(x2+alpha2*x1))))
    GammaM2 = np.exp(-np.log(x2 + alpha2*x1) - x1*((alpha1 /
                                                    (x1 + alpha1*x2)) - (alpha2/(x2+Alpha2*x1))))
    return GammaM1, GammaM2


GammaM1, GammaM2 = Calculation_Gamma(
    Constants.x1, Constants.x2, Alpha1, Alpha2)


def Model_Bubble(x1, x2, GammaM1, GammaM2):
    Constants.PBubbleMW[0] = antoniesEqn.PsatWate
    Constants.PBubbleMW[11] = antoniesEqn.PsatMeth
    Constants.PBubbleMW[1:11] = x1*GammaM1 * \
        antoniesEqn.PsatMeth + \
        x2*GammaM2*antoniesEqn.PsatWate
    return Constants.PBubbleMW


Model_Bubble(Constants.x1[1:11],Constants.x2[1:11],GammaM1[1:11],GammaM2[1:11])

# Need Model dew
