import numpy as np
import matplotlib.pyplot as plt

#Load datasets
A1 = np.loadtxt('/hand1.dat', delimiter=',')
A2 = np.loadtxt('/hand2.dat', delimiter=',')

#Calculation for matrix: A_1^T * A_2
A1t_A2 = np.dot(A1.T, A2)

#Singular Value Decomposition to find optimal rotation
U, S, Vt = np.linalg.svd(A1t_A2)

#Optimal Rotation using the Orthogonal-Procustes equation to find R
R = np.dot(U, Vt)
rotation_angle = np.degrees(np.arccos(R[0, 0]))
if R[1, 0] < 0:
    rotation_angle = -rotation_angle
A2_rotated = np.dot(A2, R.T)

#Plotting original hand and rotated hand
plt.plot(A1[:, 0], A1[:, 1], color='red', label='Hand 1')
plt.plot(A2[:, 0], A2[:, 1], color='blue', label='Hand 2')
plt.plot(A2_rotated[:, 0], A2_rotated[:, 1], color='green', label='Hand 2 Rotated')
plt.title('Hand Shapes')
plt.legend()
plt.show()

print("Optimal rotation angle: {:.2f} degrees".format(rotation_angle))
