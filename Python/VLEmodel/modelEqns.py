import numpy as np
import ConstantsWilson
import SatLiquRacket
import objMinimization
import antoniesEqn

y1M = (ConstantsWilson.x1_Willson * ConstantsWilson.GammaE1_Willson *
       antoniesEqn.PsatMeth)/ConstantsWilson.PBubble_Willson
y2M = 1 - y1M


def Wilson_Constants():
    Wil_Constants = objMinimization.optimize_Results()
    Vl1, Vl2 = SatLiquRacket.SatLiqVolumeRacket(
        ConstantsWilson.Vl1_Wilson, ConstantsWilson.Vl2_Wilson, ConstantsWilson.ZcMeth_Willson, ConstantsWilson.ZcWate_Willson, ConstantsWilson.Tr1, ConstantsWilson.Tr2)
    Alph1 = (Vl2/Vl1) * \
        np.exp(-Wil_Constants[0]/(ConstantsWilson.R*ConstantsWilson.T_Willson))
    Alph2 = (Vl1/Vl2) * \
        np.exp(-Wil_Constants[1]/(ConstantsWilson.R*ConstantsWilson.T_Willson))
    return Alph1, Alph2

Wilson_Constants()

Alpha1, Alpha2 = Wilson_Constants()


def Wilson_GibbsEx():
    ConstantsWilson.GEM_Wilson[1:ConstantsWilson.end-1] = (-ConstantsWilson.x1_Willson[1:ConstantsWilson.end-1] *
                                                           np.log(ConstantsWilson.x1_Willson[1:ConstantsWilson.end-1] + Alpha1 *
                                                                  ConstantsWilson.x2_Willson [1:ConstantsWilson.end-1]) - ConstantsWilson.x2_Willson [1:ConstantsWilson.end-1] *
                                                           np.log(ConstantsWilson.x2_Willson [1:ConstantsWilson.end-1] + Alpha2 * ConstantsWilson.x1_Willson[1:ConstantsWilson.end-1]))
    return ConstantsWilson.GEM_Wilson


Wilson_GibbsEx()


def Calculation_Gamma(x1, x2, alpha1, alpha2):
    GammaM1 = np.exp(-np.log(x1 + alpha1*x2) + x2*((alpha1 /
                                                    (x1 + alpha1*x2)) - (alpha2/(x2+alpha2*x1))))
    GammaM2 = np.exp(-np.log(x2 + alpha2*x1) - x1*((alpha1 /
                                                    (x1 + alpha1*x2)) - (alpha2/(x2+Alpha2*x1))))
    return GammaM1, GammaM2


Calculation_Gamma(
    ConstantsWilson.x1_Willson, ConstantsWilson.x2_Willson , Alpha1, Alpha2)


def Model_Bubble(x1, x2, GammaM1, GammaM2, Psat1, Psat2):
    ConstantsWilson.PBubbleM_Willson[0] = Psat2
    ConstantsWilson.PBubbleM_Willson[11] = Psat1
    ConstantsWilson.PBubbleM_Willson[1:ConstantsWilson.end-1] = x1*GammaM1 * \
        Psat1 + \
        x2*GammaM2*Psat2
    return ConstantsWilson.PBubbleM_Willson


Model_Bubble(ConstantsWilson.x1_Willson[1:ConstantsWilson.end-1], ConstantsWilson.x2_Willson [1:ConstantsWilson.end-1],
             Calculation_Gamma(
    ConstantsWilson.x1_Willson, ConstantsWilson.x2_Willson , Alpha1, Alpha2)[0][1:ConstantsWilson.end-1], Calculation_Gamma(
    ConstantsWilson.x1_Willson, ConstantsWilson.x2_Willson , Alpha1, Alpha2)[1][1:ConstantsWilson.end-1], antoniesEqn.PsatMeth, antoniesEqn.PsatWate)


def Model_Dew(y1, y2, Psat1, Psat2):
    ConstantsWilson.PDeWM_Willson[0] = Psat2
    ConstantsWilson.PDeWM_Willson[11] = Psat1
    ConstantsWilson.PDeWM_Willson[1:ConstantsWilson.end-1] = 1 / \
        ((y1[1:ConstantsWilson.end-1]/Psat1) +
         (y2[1:ConstantsWilson.end-1]/Psat2))
    return ConstantsWilson.PDeWM_Willson


Model_Dew(y1M, y2M,
          antoniesEqn.PsatMeth, antoniesEqn.PsatWate)
