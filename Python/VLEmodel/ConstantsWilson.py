import numpy as np
import pandas as pd

loadData1_Willson = pd.read_excel(
    r'C:\Users\solid\Documents\MATLAB\MATLAB\MATLAB\MethanolWater.xlsx')
loadDataArray1 = loadData1_Willson.to_numpy()

# Data
P_Willson = loadDataArray1[0:12, 0]
x1_Willson = loadDataArray1[0:12, 1]
x2_Willson = 1 - x1_Willson
y1E_Willson = loadDataArray1[0:12, 2]
y2E_Willson = 1 - y1E_Willson
end = len(P_Willson)

# Global Constants
Tref_Willson = 273.15
T_Willson = 333.15
Tc1_Willson = 512.5
Tc2_Willson = 647.27
R = 83.14
Tr1 = T_Willson/Tc1_Willson
Tr2 = T_Willson/Tc2_Willson
GammaE1_Willson = np.zeros(12)
GammaE2_Willson = np.zeros(12)
GEE_Willson = np.zeros(12)
Vl1_Wilson = 114
Vl2_Wilson = 56
xguess = [5, 5]
PBubble_Willson = np.zeros(12)
PDew_Willson = np.zeros(12)


# Wilson Constants
ZcMeth_Willson = 0.224
ZcWate_Willson = 0.230
GEM_Wilson = np.zeros(12)
PBubbleM_Willson = np.zeros(12)
PDeWM_Willson = np.zeros(12)
