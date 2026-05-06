import numpy as np
import matplotlib.pyplot as plt
G = 6.67e-11
m1 = 5.97e24
m2 = 1000
p1 = np.array([0.0, 0.0])
p2 = np.array([9e6, 0.0])
v1 = np.array([0.0, 0.0])
v2 = np.array([0.0, 8700])
t = 1
pos1 = []
pos2 = []
for i in range(6000):
    r = p2 - p1
    d = np.linalg.norm(r)
    f = (G * m1 * m2) / (d**2)
    direction = r / d
    acc1 = (f * direction) / m1
    acc2 = (-f * direction) / m2
    v1 += acc1 * t
    v2 += acc2 * t
    p1 += v1 * t
    p2 += v2 * t
    pos1.append(p1.copy())
    pos2.append(p2.copy())
pos1 = np.array(pos1)
pos2 = np.array(pos2)
plt.figure(figsize=(6,6))
plt.plot(pos2[:,0], pos2[:,1])
plt.plot(pos1[:,0], pos1[:,1])
plt.scatter(pos1[0,0], pos1[0,1], color='red')
plt.scatter(pos2[0,0], pos2[0,1], color='green')
plt.axis("equal")
plt.legend()
plt.title("Two-Body Interaction Simulation")
plt.show()