import ConstantsWilson
PsatMeth = (
    10**((7.89750)-((1474.08) / (229.13+(ConstantsWilson.T_Willson-ConstantsWilson.Tref_Willson))))) / 7.5006
PsatWate = (
    10**((8.01195)-((1698.785) / (231.04+(ConstantsWilson.T_Willson-ConstantsWilson.Tref_Willson))))) / 7.5006