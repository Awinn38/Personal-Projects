import matplotlib.pyplot as plt
import modelEqns
import experimentalEqns
import Constants
import antoniesEqn

Alpha1, Alpha2 = modelEqns.Wilson_Constants()
GammaM1, GammaM2 = modelEqns.Calculation_Gamma(
    Constants.x1, Constants.x2, Alpha1, Alpha2)
plt.figure()
plt.subplot(2, 1, 1)
plt.scatter(Constants.x1, experimentalEqns.Experamental_GRT(Constants.x1[1:11], Constants.x2[1:11],
                                                            Constants.GammaE1[1:11], Constants.GammaE2[1:11]), label="GEE")
plt.plot(Constants.x1, modelEqns.Wilson_GibbsEx(), label="GM_Wilson")
plt.legend(['Model','Experimental(Raoults)'])
plt.xlabel('Methanol')
plt.ylabel('GE/RT')


plt.subplot(2, 1, 2)
plt.scatter(Constants.x1, experimentalEqns.Experimental_Bubble(
    Constants.x1[1:11], Constants.x2[1:11], Constants.GammaE1[1:11], Constants.GammaE2[1:11], antoniesEqn.PsatMeth, antoniesEqn.PsatWate))
plt.scatter(Constants.x1, experimentalEqns.Experimental_Dew(
    Constants.y1E[1:11], Constants.y2E[1:11], antoniesEqn.PsatMeth, antoniesEqn.PsatWate))
plt.plot(Constants.x1, modelEqns.Model_Bubble(
    Constants.x1[1:11], Constants.x2[1:11], GammaM1[1:11], GammaM2[1:11], antoniesEqn.PsatMeth, antoniesEqn.PsatWate))
plt.plot(Constants.x1, modelEqns.Model_Dew(modelEqns.y1M, modelEqns.y2M,
          antoniesEqn.PsatMeth, antoniesEqn.PsatWate))

plt.legend(['Model Bubble','Model Dew','Experimental Bubble','Experimental Dew'])
plt.xlabel('Methanol')
plt.ylabel('Pressure(kPa)')

plt.show()
