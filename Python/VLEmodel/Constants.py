import numpy as np
import pandas as pd

loadData = pd.read_excel(
    r'C:\Users\solid\Documents\MATLAB\MATLAB\MATLAB\MethanolWater.xlsx')
loadDataArray = loadData.to_numpy()

# Data
P = loadDataArray[0:12, 0]
x1 = loadDataArray[0:12, 1]
x2 = 1 - x1
y1E = loadDataArray[0:12, 2]
y2E = 1 - y1E

# Global Constants
Tref = 273.15
T = 333.15
Tc1 = 512.5
Tc2 = 647.27
R = 83.14
Tr1 = T/Tc1
Tr2 = T/Tc2
GammaE1 = np.zeros(12)
GammaE2 = np.zeros(12)
GEE = np.zeros(12)
VlMeth = 114
VlWate = 56
xguess = [5, 5]
PBubble = np.zeros(12)
PDew = np.zeros(12)

# Wilson Constants
Zc1 = 0.224
Zc2 = 0.230
GEM_Wilson = np.zeros(12)

