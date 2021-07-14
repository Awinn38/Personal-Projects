import Constants
def SatLiqVolumeRacket(Vl1,Vl2,Zc1,Zc2,Tr1,Tr2):
    VlsatMeth =  Vl1*Zc1**((1-Tr1)**(2/7))
    VlsatWate =Vl2*Zc2**((1-Tr2)**(2/7))
    return VlsatMeth, VlsatWate
SatLiqVolumeRacket(Constants.Vl1,Constants.Vl2,Constants.Zc1,Constants.Zc2,Constants.Tr1,Constants.Tr2)