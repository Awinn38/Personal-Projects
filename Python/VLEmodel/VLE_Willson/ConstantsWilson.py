import numpy as np
import pandas as pd

loadData1_Willson = pd.read_excel(
    r'C:\Users\solid\Documents\MATLAB\MATLAB\MATLAB\MethanolWater.xlsx')
loadDataArrayWillson = loadData1_Willson.to_numpy()

# Data
P_Willson = loadDataArrayWillson[0:len(loadDataArrayWillson), 0]
x1_Willson = loadDataArrayWillson[0:len(loadDataArrayWillson), 1]
x2_Willson = 1 - x1_Willson
y1E_Willson = loadDataArrayWillson[0:len(loadDataArrayWillson), 2]
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
GammaE1_Willson = np.zeros(end)
GammaE2_Willson = np.zeros(end)
GEE = np.zeros(end)
Vl1_Wilson = 114
Vl2_Wilson = 56
xguess = [5, 5]
PBubble_Willson = np.zeros(end)
PDew_Willson = np.zeros(end)


# Wilson Constants
Zc1 = 0.224
Zc2 = 0.230
GEM_Wilson = np.zeros(end)
PBubbleM_Willson = np.zeros(end)
PDeWM_Willson = np.zeros(end)
