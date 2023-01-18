import numpy as np
import matplotlib.pyplot as plt
u = []
dx = 0.01
dt = 0.01
alfa = dt**2/dx**2
N = 100
M = 100
u.append(0)
for i in range(1,N-1):
    u.append(np.exp(-400*((dx*i-0.3)**2)))
u.append(0)
u0 = []
u3 = []
for ž in u:
    u0.append(ž)
    u3.append(ž)
print(len(u3))
u2 = [0]
u005 = []
u01 = []
u02 = []
for j in range(1,N-1):
    u2.append(u[j]+(alfa/2)*(u[j+1]-2*u[j]+u[j-1]))
u.clear()
for dž in u2:
    u.append(dž)
u.append(0)
u2.clear()
u2.append(0)
for jj in range(2,M):
    for k in range(1,N-1):
        u2.append(alfa*u[k+1]+2*(1-alfa)*u[k]+alfa*u[k-1]-u3[k])
    u3.clear()
    for f in u:
        u3.append(f)
    u2.append(0)
    u.clear()
    for l in u2:
        u.append(l)
    if jj == 5:
        for č in u:
            u005.append(č)
    if jj == 10:
        for ć in u:
            u01.append(ć)
    if jj == 20:
        for š in u:
            u02.append(š)
    u2.clear()
    u2.append(0)
xdx = []
for đ in range(0,N):
    xdx.append(dx*đ)
plt.plot(xdx,u0)
plt.plot(xdx,u005)
plt.plot(xdx,u01)
plt.plot(xdx,u02)
plt.xlabel("x [m]")
plt.ylabel("u")
plt.legend(["t = 0","t = 0.05 s","t = 0.1 s","t = 0.2 s"])
plt.title("Eksplicitna metoda")
plt.show()

    

