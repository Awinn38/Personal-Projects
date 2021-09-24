import ConstantsWilsonTemp


def SatLiqVolumeRacket(Vl1, Vl2, Zc1, Zc2, Tr1, Tr2):
    VlsatMeth = Vl1*Zc1**((1-Tr1)**(2/7))
    VlsatWate = Vl2*Zc2**((1-Tr2)**(2/7))
    return VlsatMeth, VlsatWate


SatLiqVolumeRacket(ConstantsWilsonTemp.T_WilsonTemp, ConstantsWilsonTemp.Vl2_WilsonTemp,
                   ConstantsWilsonTemp.Zc1, ConstantsWilsonTemp.Zc2, ConstantsWilsonTemp.Tr1, ConstantsWilsonTemp.Tr2)
