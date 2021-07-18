import numpy as np
import Constants
import SatLiquRacket
import objMinimization
import antoniesEqn
import experimentalEqns

[GammaE1,GammE2] = experimentalEqns.Experamental_Gamma(Constants.P[1:11], Constants.x1[1:11], Constants.x2[1:11],
                   Constants.y1E[1:11], Constants.y2E[1:11], antoniesEqn.PsatMeth, antoniesEqn.PsatWate)
y1M = (Constants.x1 *Constants.GammaE1*antoniesEqn.PsatMeth)/Constants.PBubble
y2M = 1 - y1M

def Wilson_Constants():
    Wil_Constants = objMinimization.optimize_Results()
    Vl1, Vl2 = SatLiquRacket.SatLiqVolumeRacket(
        Constants.Vl1, Constants.Vl2, Constants.Zc1, Constants.Zc2, Constants.Tr1, Constants.Tr2)
    Alph1 = (Vl2/Vl1)*np.exp(-Wil_Constants[0]/(Constants.R*Constants.T))
    Alph2 = (Vl1/Vl2)*np.exp(-Wil_Constants[1]/(Constants.R*Constants.T))
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


def Model_Bubble(x1, x2, GammaM1, GammaM2, Psat1, Psat2):
    Constants.PBubbleMW[0] = Psat2
    Constants.PBubbleMW[11] = Psat1
    Constants.PBubbleMW[1:11] = x1*GammaM1 * \
        Psat1 + \
        x2*GammaM2*Psat2
    return Constants.PBubbleMW


Model_Bubble(Constants.x1[1:11], Constants.x2[1:11],
             GammaM1[1:11], GammaM2[1:11],antoniesEqn.PsatMeth,antoniesEqn.PsatWate)


def Model_Dew(y1, y2, Psat1, Psat2):
    Constants.PDewM[0] = Psat2
    Constants.PDewM[11] = Psat1
    Constants.PDewM[1:11] = 1 / ((y1[1:11]/Psat1) + (y2[1:11]/Psat2))
    return Constants.PDewM


Model_Dew(y1M, y2M,
          antoniesEqn.PsatMeth, antoniesEqn.PsatWate)