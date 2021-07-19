import numpy as np
import pandas as pd

loadData1_Willson = pd.read_excel(
    r'C:\Users\solid\Documents\MATLAB\MATLAB\MATLAB\EthanolEther.xlsx')
loadDataArrayWillsonTemp = loadData1_Willson.to_numpy()

# Data
P_WilsonTemp = loadDataArrayWillsonTemp[0:len(loadDataArrayWillsonTemp), 1]
x1_WilsonTemp = loadDataArrayWillsonTemp[0:len(loadDataArrayWillsonTemp), 0]
x2_WilsonTemp = 1 - x1_WilsonTemp
y1E_WilsonTemp = loadDataArrayWillsonTemp[0:len(loadDataArrayWillsonTemp), 2]
y2E_WilsonTemp = 1 - y1E_WilsonTemp
end = len(P_WilsonTemp)

# Global Constants
Tref_WillsonTemp = 273.15
T_WilsonTemp = 323.15
Tc1_WilsonTemp = 512.5
Tc2_WillsonTemp = 647.27
R = 83.14
Tr1 = T_WilsonTemp/Tc1_WilsonTemp
Tr2 = T_WilsonTemp/Tc2_WillsonTemp
GammaE1_WilsonTemp = np.zeros(end)
GammaE2_WilsonTemp = np.zeros(end)
GEE = np.zeros(end)
Vl1_WilsonTemp = 114
Vl2_WilsonTemp = 56
xguess = [5, 5]
PBubble_WilsonTemp = np.zeros(end)
PDew_WilsonTemp = np.zeros(end)


# Wilson Constants
Zc1 = 0.224
Zc2 = 0.230
GEM_WilsonTemp = np.zeros(end)
PBubbleM_WilsonTemp = np.zeros(end)
PDeWM_WilsonTemp = np.zeros(end)
