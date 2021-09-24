import ConstantsWilson


def SatLiqVolumeRacket(Vl1, Vl2, Zc1, Zc2, Tr1, Tr2):
    VlsatMeth = Vl1*Zc1**((1-Tr1)**(2/7))
    VlsatWate = Vl2*Zc2**((1-Tr2)**(2/7))
    return VlsatMeth, VlsatWate


SatLiqVolumeRacket(ConstantsWilson.T_Willson, ConstantsWilson.Vl2_Wilson,
                   ConstantsWilson.Zc1, ConstantsWilson.Zc2, ConstantsWilson.Tr1, ConstantsWilson.Tr2)
