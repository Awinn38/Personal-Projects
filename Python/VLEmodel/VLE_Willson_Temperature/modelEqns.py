import numpy as np
import ConstantsWilsonTemp
import SatLiquRacket
import objMinimization
import antoniesEqn

y1M = (ConstantsWilsonTemp.x1_WilsonTemp * ConstantsWilsonTemp.GammaE1_WilsonTemp *
       antoniesEqn.PsatMeth)/ConstantsWilsonTemp.PBubbleM_WilsonTemp
y2M = 1 - y1M


def Wilson_Constants():
    Wil_Constants = objMinimization.optimize_Results()
    Vl1, Vl2 = SatLiquRacket.SatLiqVolumeRacket(
        ConstantsWilsonTemp.Vl1_WilsonTemp, ConstantsWilsonTemp.Vl2_WilsonTemp, ConstantsWilsonTemp.Zc1, ConstantsWilsonTemp.Zc2, ConstantsWilsonTemp.Tr1, ConstantsWilsonTemp.Tr2)
    Alph1 = (Vl2/Vl1) * \
        np.exp(-Wil_Constants[0]/(ConstantsWilsonTemp.R *
                                  ConstantsWilsonTemp.T_WilsonTemp))
    Alph2 = (Vl1/Vl2) * \
        np.exp(-Wil_Constants[1]/(ConstantsWilsonTemp.R *
                                  ConstantsWilsonTemp.T_WilsonTemp))
    return Alph1, Alph2


Wilson_Constants()

Alpha1, Alpha2 = Wilson_Constants()


def Wilson_GibbsEx():
    ConstantsWilsonTemp.GEM_WilsonTemp[1:ConstantsWilsonTemp.end-1] = (-ConstantsWilsonTemp.x1_WilsonTemp[1:ConstantsWilsonTemp.end-1] *
                                                                       np.log(ConstantsWilsonTemp.x1_WilsonTemp[1:ConstantsWilsonTemp.end-1] + Alpha1 *
                                                                              ConstantsWilsonTemp.x2_WilsonTemp[1:ConstantsWilsonTemp.end-1]) - ConstantsWilsonTemp.x2_WilsonTemp[1:ConstantsWilsonTemp.end-1] *
                                                                       np.log(ConstantsWilsonTemp.x2_WilsonTemp[1:ConstantsWilsonTemp.end-1] + Alpha2 * ConstantsWilsonTemp.x1_WilsonTemp[1:ConstantsWilsonTemp.end-1]))
    return ConstantsWilsonTemp.GEM_WilsonTemp


Wilson_GibbsEx()


def Calculation_Gamma(x1, x2, alpha1, alpha2):
    GammaM1 = np.exp(-np.log(x1 + alpha1*x2) + x2*((alpha1 /
                                                    (x1 + alpha1*x2)) - (alpha2/(x2+alpha2*x1))))
    GammaM2 = np.exp(-np.log(x2 + alpha2*x1) - x1*((alpha1 /
                                                    (x1 + alpha1*x2)) - (alpha2/(x2+Alpha2*x1))))
    return GammaM1, GammaM2


Calculation_Gamma(
    ConstantsWilsonTemp.x1_WilsonTemp, ConstantsWilsonTemp.x2_WilsonTemp, Alpha1, Alpha2)


def Model_Bubble(x1, x2, GammaM1, GammaM2, Psat1, Psat2):
    ConstantsWilsonTemp.PBubbleM_WilsonTemp[0] = Psat2
    ConstantsWilsonTemp.PBubbleM_WilsonTemp[ConstantsWilsonTemp.end-1] = Psat1
    ConstantsWilsonTemp.PBubbleM_WilsonTemp[1:ConstantsWilsonTemp.end-1] = x1*GammaM1 * \
        Psat1 + \
        x2*GammaM2*Psat2

    return ConstantsWilsonTemp.PBubbleM_WilsonTemp


Model_Bubble(ConstantsWilsonTemp.x1_WilsonTemp[1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.x2_WilsonTemp[1:ConstantsWilsonTemp.end-1],
             Calculation_Gamma(
    ConstantsWilsonTemp.x1_WilsonTemp, ConstantsWilsonTemp.x2_WilsonTemp, Alpha1, Alpha2)[0][1:ConstantsWilsonTemp.end-1], Calculation_Gamma(
    ConstantsWilsonTemp.x1_WilsonTemp, ConstantsWilsonTemp.x2_WilsonTemp, Alpha1, Alpha2)[1][1:ConstantsWilsonTemp.end-1], antoniesEqn.PsatMeth, antoniesEqn.PsatWate)


def Model_Dew(y1, y2, Psat1, Psat2):
    ConstantsWilsonTemp.PDeWM_WilsonTemp[0] = Psat2
    ConstantsWilsonTemp.PDeWM_WilsonTemp[ConstantsWilsonTemp.end-1] = Psat1
    ConstantsWilsonTemp.PDeWM_WilsonTemp[1:ConstantsWilsonTemp.end-1] = 1 / \
        ((y1[1:ConstantsWilsonTemp.end-1]/Psat1) +
         (y2[1:ConstantsWilsonTemp.end-1]/Psat2))
    return ConstantsWilsonTemp.PDeWM_WilsonTemp


Model_Dew(y1M, y2M,
          antoniesEqn.PsatMeth, antoniesEqn.PsatWate)
