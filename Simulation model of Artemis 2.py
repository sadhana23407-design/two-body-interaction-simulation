import numpy as np
import matplotlib.pyplot as plt
G=6.67e-11
m1=5.97e24
m2=1000
p1=np.array([0.0,0.0])
p2=np.array([9e6,0.0])
v1=np.array([0.0,0.0])
v2=np.array([0.0,8700])
t=1
pos=[]
for i in range(6000):
    r=p2-p1
    d=np.linalg.norm(r)
    f=(G*m1*m2)/(d**2)
    dir=r/d
    acc=(-f*dir)/m2
    v2+=acc*t
    p2+=v2*t
    pos.append(p2.copy())
pos=np.array(pos)
plt.plot(pos[:,0],pos[:,1])
plt.scatter(0,0,color='red')
plt.axis("equal")
plt.title("Gravity between Two celestial bodies simulation")
plt.show()
d=np.linalg.norm(pos,axis=1)
periapsis=np.min(d)
apoapsis = np.max(d)
print("Periapsis: ", periapsis)
print("Apoapsis: ",apoapsis)
st_d = d[0]
period_index = None

for j in range(1, len(d)):
    if abs(d[j] - st_d) < 1e5:
        period_index = j
        break

if period_index:
    orbital_per = period_index * t
    print("Orbital period is approximately:", orbital_per, "secs")