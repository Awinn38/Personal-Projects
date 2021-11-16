import ConstantsWilson
PsatMeth = (
    10**((7.89750)-((1474.08) / (229.13+(ConstantsWilson.T_Willson-ConstantsWilson.Tref_Willson))))) / 7.5006
PsatWate = (
    10**((8.01195)-((1698.785) / (231.04+(ConstantsWilson.T_Willson-ConstantsWilson.Tref_Willson))))) / 7.5006

### Design Project 
PsatH20 = (
    10**((3.55959)-((643.748) / (460+(-198.043))))) / 7.5006
PsatPropyleneGlycol = (
    10**((6.07936)-((2692.187) / (460+(-17.94))))) / 7.5006