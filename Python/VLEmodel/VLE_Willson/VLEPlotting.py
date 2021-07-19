import matplotlib.pyplot as plt
import modelEqns
import experimentalEqns
import ConstantsWilson
import antoniesEqn


plt.figure()
plt.subplot(2, 1, 1)
plt.scatter(ConstantsWilson.x1_Willson, experimentalEqns.Experamental_GRT(ConstantsWilson.x1_Willson[1:ConstantsWilson.end-1], ConstantsWilson.x2_Willson[1:ConstantsWilson.end-1],
                                                                          ConstantsWilson.GammaE1_Willson[1:ConstantsWilson.end-1], ConstantsWilson.GammaE2_Willson[1:ConstantsWilson.end-1]), label="GEE")
plt.plot(ConstantsWilson.x1_Willson,
         modelEqns.Wilson_GibbsEx(), label="GM_Wilson")
plt.legend(['Model', 'Experimental(Raoults)'])
plt.xlabel('Methanol')
plt.ylabel('GE/RT')


plt.subplot(2, 1, 2)
plt.scatter(ConstantsWilson.x1_Willson, experimentalEqns.Experimental_Bubble(
    ConstantsWilson.x1_Willson[1:ConstantsWilson.end-1], ConstantsWilson.x2_Willson[1:ConstantsWilson.end-1], ConstantsWilson.GammaE1_Willson[1:ConstantsWilson.end-1], ConstantsWilson.GammaE2_Willson[1:ConstantsWilson.end-1], antoniesEqn.PsatMeth, antoniesEqn.PsatWate))
plt.scatter(ConstantsWilson.x1_Willson, experimentalEqns.Experimental_Dew(
    ConstantsWilson.y1E_Willson[1:ConstantsWilson.end-1], ConstantsWilson.y2E_Willson[1:ConstantsWilson.end-1], antoniesEqn.PsatMeth, antoniesEqn.PsatWate))
plt.plot(ConstantsWilson.x1_Willson, modelEqns.Model_Bubble(
    ConstantsWilson.x1_Willson[1:ConstantsWilson.end-1], ConstantsWilson.x2_Willson[1:ConstantsWilson.end-1], modelEqns.Calculation_Gamma(
        ConstantsWilson.x1_Willson, ConstantsWilson.x2_Willson, modelEqns.Wilson_Constants()[0], modelEqns.Wilson_Constants()[1])[0][1:ConstantsWilson.end-1], modelEqns.Calculation_Gamma(
        ConstantsWilson.x1_Willson, ConstantsWilson.x2_Willson, modelEqns.Wilson_Constants()[0], modelEqns.Wilson_Constants()[1])[1][1:ConstantsWilson.end-1], antoniesEqn.PsatMeth, antoniesEqn.PsatWate))
plt.plot(ConstantsWilson.x1_Willson, modelEqns.Model_Dew(modelEqns.y1M, modelEqns.y2M,
                                                         antoniesEqn.PsatMeth, antoniesEqn.PsatWate))

plt.legend(['Model Bubble', 'Model Dew',
            'Experimental Bubble', 'Experimental Dew'])
plt.xlabel('Methanol')
plt.ylabel('Pressure(kPa)')

plt.show()
