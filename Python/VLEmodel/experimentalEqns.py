import numpy as np
import pandas as pd
import Constants
import antoniesEqn

def Experamental_Gamma(P,x1,x2,y1E,y2E,PsatMeth,PsatWate):
    Constants.GammaE1[1:11] = (y1E*P)/(x1*PsatMeth)
    Constants.GammaE2[1:11] = ((y2E*P)/(x2*PsatWate))
    # return Constants.GammaE1, Constants.GammaE2

Experamental_Gamma(Constants.P[1:11],Constants.x1[1:11],Constants.x2[1:11],Constants.y1E[1:11],Constants.y2E[1:11],antoniesEqn.PsatMeth,antoniesEqn.PsatWate)
#x,y = Experamental_Gamma(Constants.P,Constants.x1,Constants.x2,Constants.y1E,Constants.y2E) Gives Return Values

def Experamental_GRT(x1,x2,GammaE1,GammaE2):
    Constants.GEE[1:11] = (x1*np.log(GammaE1)) + (x2*np.log(GammaE2))
Experamental_GRT(Constants.x1[1:11],Constants.x2[1:11],Constants.GammaE1[1:11],Constants.GammaE2[1:11])