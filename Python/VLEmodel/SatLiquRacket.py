import Constants
def SatLiqVolumeRacket(Vl1,Vl2,Zc1,Zc2,Tr1,Tr2):
    VlsatMeth =  Constants.VlMeth*Constants.Zc1**((1-Constants.Tr1)**(2/7))
    VlsatWate = Constants.VlWate*Constants.Zc2**((1-Constants.Tr2)**(2/7))
SatLiqVolumeRacket(Constants.Vl1,Constants.Vl2,Constants.Zc1,Constants.Zc2,Constants.Tr1,Constants.Tr2)