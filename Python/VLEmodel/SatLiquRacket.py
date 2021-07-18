import ConstantsWilson


def SatLiqVolumeRacket(Vl1, Vl2, ZcMeth, ZcWate, Tr1, Tr2):
    VlsatMeth = Vl1*ZcMeth**((1-Tr1)**(2/7))
    VlsatWate = Vl2*ZcWate**((1-Tr2)**(2/7))
    return VlsatMeth, VlsatWate


SatLiqVolumeRacket(ConstantsWilson.T_Willson, ConstantsWilson.Vl2_Wilson,
                   ConstantsWilson.ZcMeth_Willson, ConstantsWilson.ZcWate_Willson, ConstantsWilson.Tr1, ConstantsWilson.Tr2)
