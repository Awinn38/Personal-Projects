import Constants
PsatMeth = (10**((7.89750)-((1474.08)/(229.13+(Constants.T-Constants.Tref)))))/7.5006 
PsatWate = (10**((8.01195)-((1698.785)/(231.04+(Constants.T-Constants.Tref)))))/7.5006
print(PsatMeth)
print(PsatWate)