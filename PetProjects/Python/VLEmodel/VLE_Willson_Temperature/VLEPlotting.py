import matplotlib.pyplot as plt
import modelEqns
import experimentalEqns
import ConstantsWilsonTemp
import antoniesEqn


plt.figure()
plt.subplot(2, 1, 1)
plt.scatter(ConstantsWilsonTemp.x1_WilsonTemp, experimentalEqns.Experamental_GRT(ConstantsWilsonTemp.x1_WilsonTemp[1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.x2_WilsonTemp [1:ConstantsWilsonTemp.end-1],
                                                                  ConstantsWilsonTemp.GammaE1_WilsonTemp[1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.GammaE2_WilsonTemp[1:ConstantsWilsonTemp.end-1]), label="GEE")
plt.plot(ConstantsWilsonTemp.x1_WilsonTemp, modelEqns.Wilson_GibbsEx(), label="GM_Wilson")
plt.legend(['Model', 'Experimental(Raoults)'])
plt.xlabel('Methanol')
plt.ylabel('GE/RT')


plt.subplot(2, 1, 2)
plt.scatter(ConstantsWilsonTemp.x1_WilsonTemp, experimentalEqns.Experimental_Bubble(
    ConstantsWilsonTemp.x1_WilsonTemp[1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.x2_WilsonTemp [1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.GammaE1_WilsonTemp[1:ConstantsWilsonTemp.end-1],
                    ConstantsWilsonTemp.GammaE2_WilsonTemp[1:ConstantsWilsonTemp.end-1], antoniesEqn.PsatMeth, antoniesEqn.PsatWate))
plt.scatter(ConstantsWilsonTemp.x1_WilsonTemp, experimentalEqns.Experimental_Dew(ConstantsWilsonTemp.y1E_WilsonTemp[1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.y2E_WilsonTemp[1:ConstantsWilsonTemp.end-1],
                 antoniesEqn.PsatMeth, antoniesEqn.PsatWate))
plt.plot(ConstantsWilsonTemp.x1_WilsonTemp, modelEqns.Model_Bubble(
    ConstantsWilsonTemp.x1_WilsonTemp[1:ConstantsWilsonTemp.end-1], ConstantsWilsonTemp.x2_WilsonTemp [1:ConstantsWilsonTemp.end-1], modelEqns.Calculation_Gamma(
        ConstantsWilsonTemp.x1_WilsonTemp, ConstantsWilsonTemp.x2_WilsonTemp , modelEqns.Wilson_Constants()[0], modelEqns.Wilson_Constants()[1])[0][1:ConstantsWilsonTemp.end-1], modelEqns.Calculation_Gamma(
    ConstantsWilsonTemp.x1_WilsonTemp, ConstantsWilsonTemp.x2_WilsonTemp , modelEqns.Wilson_Constants()[0], modelEqns.Wilson_Constants()[1])[1][1:ConstantsWilsonTemp.end-1], antoniesEqn.PsatMeth, antoniesEqn.PsatWate))
plt.plot(ConstantsWilsonTemp.x1_WilsonTemp, modelEqns.Model_Dew(modelEqns.y1M, modelEqns.y2M,
                                                 antoniesEqn.PsatMeth, antoniesEqn.PsatWate))

plt.legend(['Model Bubble', 'Model Dew',
            'Experimental Bubble', 'Experimental Dew'])
plt.xlabel('Methanol')
plt.ylabel('Pressure(kPa)')

plt.show()
