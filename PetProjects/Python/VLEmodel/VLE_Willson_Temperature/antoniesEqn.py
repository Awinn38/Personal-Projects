import ConstantsWilsonTemp
PsatMeth = (
    10**((7.89750)-((1474.08) / (229.13+(ConstantsWilsonTemp.T_WilsonTemp-ConstantsWilsonTemp.Tref_WillsonTemp))))) / 7.5006
PsatWate = (
    10**((8.01195)-((1698.785) / (231.04+(ConstantsWilsonTemp.T_WilsonTemp-ConstantsWilsonTemp.Tref_WillsonTemp))))) / 7.5006
