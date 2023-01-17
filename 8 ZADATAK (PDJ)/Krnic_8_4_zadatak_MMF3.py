import numpy as np
import matplotlib.pyplot as plt
#cranknicholson
def thomas(a,b,c,d,N):
    c_cc = []
    d_cc = []
    X = np.zeros(N,dtype="float32")
    c_cc.append(c[0]/b[0])
    d_cc.append(d[0]/b[0])
    for i in range(1,N):
        c_cc.append((c[i])/(b[i]-a[i]*c_cc[i-1]))
        d_cc.append((d[i]-a[i]*d_cc[i-1])/(b[i]-a[i]*c_cc[i-1]))
    X[(N-1)] = d_cc[N-1]
    for j in range(N-2,-1,-1):
        X[j] = (d_cc[j]-c_cc[j]*X[j+1])
    return X
L = 20
D = 0.01
N = 100
dx = L/(N+1)
dt = 0.5
t0 = 0
tN = 200
alfa = D*dt/(dx**2)
M = int((tN-t0)/dt)+1
x0 = 0
poc = 0
x_lista = [x0]
x = 0
u = []
#2I - alfa*B:
A1 = []
B1 = []
C1 = [0]
A2 = []
B2 = []
C2 = [0]
for i in range(0,N):
    A1.append(alfa)
    B1.append(2*(1-alfa))
    C1.append(alfa)
    A2.append(-alfa)
    B2.append(2*(alfa+1))
    C2.append(-alfa)
del A1[N-1]
del A2[N-1]
del C1[N-1]
del C2[N-1]
A1.append(0)
A2.append(0)
for i in range(1,N):
    x_lista.append(i*dx)
    x = x_lista[i-1]
    if x < 2:
        u.append(0)
x_lista.clear()
x_lista = [x0]
for j in range(1,N):
    x_lista.append(j*dx)
    x = x_lista[j-1]
    if x >=2 and x<= 5:
        u.append(5.5)
x_lista.clear()
x_lista = [x0]
for k in range(1,N):
    x_lista.append(k*dx)
    x = x_lista[k]
    if x > 5:
        u.append(0)
x_lista.clear()
x_lista = [x0]
u2 = [A1[0]*u[1]+B1[0]*u[0]]
t = [t0]
u0 = []
u100 = []
u200 = []
u300 = []
u400 = []
for žnj in u:
    u0.append(žnj)
for z in range(1,M):
    for ž in range(1,N-1):
        u2.append(A1[ž]*u[ž+1]+B1[ž]*u[ž]+C1[ž]*u[ž-1])
    u2.append(B1[99]*u[99]+C1[99]*u[98])
    for zž in range(1,N):
        v = thomas(A2,B2,C2,u2,N)
    u.clear()
    for š in v:
        u.append(š)
    if z == 100:
        for hh in u:
            u100.append(hh)
    elif z == 200:
        for gg in u:
            u200.append(gg)
    elif z == 300:
        for ff in u:
            u300.append(ff)
    elif z == 400:
        for ss in u:
            u400.append(ss) 
    u2.clear()
    u2.append(A1[0]*u[1]+B1[0]*u[0])
print(u)
x_dx = []
for haha in range(0,N):
    x_dx.append(haha*dx)
    x = haha*dx
    if x > 20:
        break
plt.plot(x_dx,u100)
plt.plot(x_dx,u200)
plt.plot(x_dx,u300)
plt.plot(x_dx,u400)
plt.title("Crank-Nicholsonova metoda")
plt.show()



    
        
        
        
