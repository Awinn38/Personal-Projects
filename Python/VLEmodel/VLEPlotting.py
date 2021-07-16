import matplotlib.pyplot as plt
import modelEqns
import experimentalEqns
import Constants
import antoniesEqn

plt.figure()
plt.subplot(2, 1, 1)
plt.scatter(Constants.x1, experimentalEqns.Experamental_GRT(Constants.x1[1:11], Constants.x2[1:11],
                                                            Constants.GammaE1[1:11], Constants.GammaE2[1:11]), label="GEE")
plt.plot(Constants.x1, modelEqns.Wilson_GibbsEx(), label="GM_Wilson")
plt.legend()
plt.xlabel('x Methanol')
plt.ylabel('Gibbs Comparison')


plt.subplot(2, 1, 2)
plt.scatter(Constants.x1, experimentalEqns.Experimental_Bubble(
    Constants.x1[1:11], Constants.x2[1:11], Constants.GammaE1[1:11], Constants.GammaE2[1:11], antoniesEqn.PsatMeth, antoniesEqn.PsatWate))
plt.scatter(Constants.x1, experimentalEqns.Experimental_Dew(
    Constants.y1E[1:11], Constants.y2E[1:11], antoniesEqn.PsatMeth, antoniesEqn.PsatWate))

plt.show()
