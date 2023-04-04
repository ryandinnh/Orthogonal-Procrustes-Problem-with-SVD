import numpy as np
import matplotlib.pyplot as plt

A1 = np.loadtxt('/hand1.dat', delimiter=',')
A2 = np.loadtxt('/hand2.dat', delimiter=',')

fig, ax = plt.subplots()

#Matrix A1, color BLUE
ax.plot(A1[:, 0], A1[:, 1], color='blue')

#Matrix A2, color RED
ax.plot(A2[:, 0], A2[:, 1], color='red')

#Connecting consecutive points to create hand outline
ax.plot([A1[:, 0], np.roll(A1[:, 0], -1)], [A1[:, 1], np.roll(A1[:, 1], -1)], color='blue')
ax.plot([A2[:, 0], np.roll(A2[:, 0], -1)], [A2[:, 1], np.roll(A2[:, 1], -1)], color='red')

ax.set_title('Hand Shapes: A1, A2')
plt.show()
