############################################################
#
#    polynomials
#
############################################################

import numpy as np
import matplotlib.pyplot as plt

""" calculate polynomial: y = -2x^2 + 1 """

X = np.arange(-4, 4, 0.01)
Y = [-2*a**2+1 for a in X]

ax = plt.subplot()
ax.plot(X, Y, color='red', lw=1)
plt.gcf().canvas.set_window_title('Calculate Polynomial')

plt.show()

