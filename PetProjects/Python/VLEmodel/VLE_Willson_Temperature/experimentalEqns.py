# import numpy as np
# import ConstantsWilsonTemp
# import antoniesEqn


# def Experamental_Gamma(P_WilsonTemp, x1, x2, y1E, y2E, PsatMeth, PsatWate):
#     ConstantsWilsonTemp.GammaE1_WilsonTemp[1:ConstantsWilsonTemp.end-1] = (y1E*P_WilsonTemp)/(x1*PsatMeth)
#     ConstantsWilsonTemp.GammaE2_WilsonTemp[1:ConstantsWilsonTemp.end-1] = ((y2E*P_WilsonTemp)/(x2*PsatWate))
#     return ConstantsWilsonTemp.GammaE1_WilsonTemp[1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.GammaE2_WilsonTemp[1:ConstantsWilsonTemp.end-1]

# Experamental_Gamma(ConstantsWilsonTemp.P_WilsonTemp[1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.x1_WilsonTemp[1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.x2_WilsonTemp [1:ConstantsWilsonTemp.end-1],
#                    ConstantsWilsonTemp.y1E_WilsonTemp[1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.y2E_WilsonTemp[1:ConstantsWilsonTemp.end-1], antoniesEqn.PsatMeth, antoniesEqn.PsatWate)


# def Experamental_GRT(x1, x2, GammaE1, GammaE2):
#     ConstantsWilsonTemp.GEE[1:ConstantsWilsonTemp.end-1] = (x1*np.log(GammaE1)) + (x2*np.log(GammaE2))
#     return ConstantsWilsonTemp.GEE


# Experamental_GRT(ConstantsWilsonTemp.x1_WilsonTemp[1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.x2_WilsonTemp [1:ConstantsWilsonTemp.end-1],
#                  ConstantsWilsonTemp.GammaE1_WilsonTemp[1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.GammaE2_WilsonTemp[1:ConstantsWilsonTemp.end-1])


# def Experimental_Bubble(x1, x2, GammaE1, GammaE2, PsatMeth, PsatWate):
#     ConstantsWilsonTemp.PBubble_WilsonTemp[0] = antoniesEqn.PsatWate
#     ConstantsWilsonTemp.PBubble_WilsonTemp[ConstantsWilsonTemp.end-1]= antoniesEqn.PsatMeth
#     ConstantsWilsonTemp.PBubble_WilsonTemp[1:ConstantsWilsonTemp.end-1] = x1*GammaE1*PsatMeth + x2*GammaE2*PsatWate
#     return ConstantsWilsonTemp.PBubble_WilsonTemp


# Experimental_Bubble(ConstantsWilsonTemp.x1_WilsonTemp[1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.x2_WilsonTemp [1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.GammaE1_WilsonTemp[1:ConstantsWilsonTemp.end-1],
#                     ConstantsWilsonTemp.GammaE2_WilsonTemp[1:ConstantsWilsonTemp.end-1], antoniesEqn.PsatMeth, antoniesEqn.PsatWate)


# def Experimental_Dew(y1E, y2E, PsatMeth, PsatWate):
#     ConstantsWilsonTemp.PDew_WilsonTemp[0] = antoniesEqn.PsatWate
#     ConstantsWilsonTemp.PDew_WilsonTemp[ConstantsWilsonTemp.end-1] = antoniesEqn.PsatMeth
#     ConstantsWilsonTemp.PDew_WilsonTemp[1:ConstantsWilsonTemp.end-1] = 1/(((y1E)/PsatMeth) + (y2E/PsatWate))
#     return ConstantsWilsonTemp.PDew_WilsonTemp


# Experimental_Dew(ConstantsWilsonTemp.y1E_WilsonTemp[1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.y2E_WilsonTemp[1:ConstantsWilsonTemp.end-1],
#                  antoniesEqn.PsatMeth, antoniesEqn.PsatWate)


import numpy as np
import ConstantsWilsonTemp
import antoniesEqn


def Experamental_Gamma(P_Willson, x1, x2, y1E, y2E, PsatMeth, PsatWate):
    ConstantsWilsonTemp.GammaE1_WilsonTemp[1:ConstantsWilsonTemp.end-1] = (y1E*P_Willson)/(x1*PsatMeth)
    ConstantsWilsonTemp.GammaE2_WilsonTemp[1:ConstantsWilsonTemp.end-1] = ((y2E*P_Willson)/(x2*PsatWate))
    return ConstantsWilsonTemp.GammaE1_WilsonTemp[1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.GammaE2_WilsonTemp[1:ConstantsWilsonTemp.end-1]

Experamental_Gamma(ConstantsWilsonTemp.P_WilsonTemp[1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.x1_WilsonTemp[1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.x2_WilsonTemp [1:ConstantsWilsonTemp.end-1],
                   ConstantsWilsonTemp.y1E_WilsonTemp[1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.y2E_WilsonTemp[1:ConstantsWilsonTemp.end-1], antoniesEqn.PsatMeth, antoniesEqn.PsatWate)


def Experamental_GRT(x1, x2, GammaE1, GammaE2):
    ConstantsWilsonTemp.GEE[1:ConstantsWilsonTemp.end-1] = (x1*np.log(GammaE1)) + (x2*np.log(GammaE2))
    return ConstantsWilsonTemp.GEE


Experamental_GRT(ConstantsWilsonTemp.x1_WilsonTemp[1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.x2_WilsonTemp [1:ConstantsWilsonTemp.end-1],
                 ConstantsWilsonTemp.GammaE1_WilsonTemp[1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.GammaE2_WilsonTemp[1:ConstantsWilsonTemp.end-1])


def Experimental_Bubble(x1, x2, GammaE1, GammaE2, PsatMeth, PsatWate):
    ConstantsWilsonTemp.PBubbleM_WilsonTemp[0] = antoniesEqn.PsatWate
    ConstantsWilsonTemp.PBubbleM_WilsonTemp[ConstantsWilsonTemp.end-1] = antoniesEqn.PsatMeth
    ConstantsWilsonTemp.PBubbleM_WilsonTemp[1:ConstantsWilsonTemp.end-1] = x1*GammaE1*PsatMeth + x2*GammaE2*PsatWate
    return ConstantsWilsonTemp.PBubbleM_WilsonTemp


Experimental_Bubble(ConstantsWilsonTemp.x1_WilsonTemp[1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.x2_WilsonTemp [1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.GammaE1_WilsonTemp[1:ConstantsWilsonTemp.end-1],
                    ConstantsWilsonTemp.GammaE2_WilsonTemp[1:ConstantsWilsonTemp.end-1], antoniesEqn.PsatMeth, antoniesEqn.PsatWate)


def Experimental_Dew(y1E, y2E, PsatMeth, PsatWate):
    ConstantsWilsonTemp.PDew_WilsonTemp[0] = antoniesEqn.PsatWate
    ConstantsWilsonTemp.PDew_WilsonTemp[ConstantsWilsonTemp.end-1] = antoniesEqn.PsatMeth
    ConstantsWilsonTemp.PDew_WilsonTemp[1:ConstantsWilsonTemp.end-1] = 1/(((y1E)/PsatMeth) + (y2E/PsatWate))
    return ConstantsWilsonTemp.PDew_WilsonTemp


Experimental_Dew(ConstantsWilsonTemp.y1E_WilsonTemp[1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.y2E_WilsonTemp[1:ConstantsWilsonTemp.end-1],
                 antoniesEqn.PsatMeth, antoniesEqn.PsatWate)