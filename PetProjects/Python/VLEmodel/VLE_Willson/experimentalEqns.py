import numpy as np
import ConstantsWilson
import antoniesEqn


def Experamental_Gamma(P_Willson, x1, x2, y1E, y2E, PsatMeth, PsatWate):
    ConstantsWilson.GammaE1_Willson[1:ConstantsWilson.end-1] = (y1E*P_Willson)/(x1*PsatMeth)
    ConstantsWilson.GammaE2_Willson[1:ConstantsWilson.end-1] = ((y2E*P_Willson)/(x2*PsatWate))
    return ConstantsWilson.GammaE1_Willson[1:ConstantsWilson.end-1], ConstantsWilson.GammaE2_Willson[1:ConstantsWilson.end-1]

Experamental_Gamma(ConstantsWilson.P_Willson[1:ConstantsWilson.end-1], ConstantsWilson.x1_Willson[1:ConstantsWilson.end-1], ConstantsWilson.x2_Willson [1:ConstantsWilson.end-1],
                   ConstantsWilson.y1E_Willson[1:ConstantsWilson.end-1], ConstantsWilson.y2E_Willson[1:ConstantsWilson.end-1], antoniesEqn.PsatMeth, antoniesEqn.PsatWate)


def Experamental_GRT(x1, x2, GammaE1, GammaE2):
    ConstantsWilson.GEE[1:ConstantsWilson.end-1] = (x1*np.log(GammaE1)) + (x2*np.log(GammaE2))
    return ConstantsWilson.GEE


Experamental_GRT(ConstantsWilson.x1_Willson[1:ConstantsWilson.end-1], ConstantsWilson.x2_Willson [1:ConstantsWilson.end-1],
                 ConstantsWilson.GammaE1_Willson[1:ConstantsWilson.end-1], ConstantsWilson.GammaE2_Willson[1:ConstantsWilson.end-1])


def Experimental_Bubble(x1, x2, GammaE1, GammaE2, PsatMeth, PsatWate):
    ConstantsWilson.PBubble_Willson[0] = antoniesEqn.PsatWate
    ConstantsWilson.PBubble_Willson[ConstantsWilson.end-1] = antoniesEqn.PsatMeth
    ConstantsWilson.PBubble_Willson[1:ConstantsWilson.end-1] = x1*GammaE1*PsatMeth + x2*GammaE2*PsatWate
    return ConstantsWilson.PBubble_Willson


Experimental_Bubble(ConstantsWilson.x1_Willson[1:ConstantsWilson.end-1], ConstantsWilson.x2_Willson [1:ConstantsWilson.end-1], ConstantsWilson.GammaE1_Willson[1:ConstantsWilson.end-1],
                    ConstantsWilson.GammaE2_Willson[1:ConstantsWilson.end-1], antoniesEqn.PsatMeth, antoniesEqn.PsatWate)


def Experimental_Dew(y1E, y2E, PsatMeth, PsatWate):
    ConstantsWilson.PDew_Willson[0] = antoniesEqn.PsatWate
    ConstantsWilson.PDew_Willson[ConstantsWilson.end-1] = antoniesEqn.PsatMeth
    ConstantsWilson.PDew_Willson[1:ConstantsWilson.end-1] = 1/(((y1E)/PsatMeth) + (y2E/PsatWate))
    return ConstantsWilson.PDew_Willson


Experimental_Dew(ConstantsWilson.y1E_Willson[1:ConstantsWilson.end-1], ConstantsWilson.y2E_Willson[1:ConstantsWilson.end-1],
                 antoniesEqn.PsatMeth, antoniesEqn.PsatWate)
