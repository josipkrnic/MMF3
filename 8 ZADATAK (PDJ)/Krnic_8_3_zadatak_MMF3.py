import numpy as np
import matplotlib.pyplot as plt
L = 20
D = 0.01
N = 100
poc = 0
dx = L/(N+1)
dt = 0.5
alfa = D*dt/(dx**2)
t0 = 0
tN = 200
M = int((tN-t0)/dt)+1
print(M)
T = M*dt
x0 = 0
x_lista = [x0]
x = 0
u = []
#eksplicitno
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
u2 = [poc]
vr = 0
t = [t0]
u0 = []
for žnj in u:
    u0.append(žnj)
del u0[99]
u100 = []
u200 = []
u300 = []
u400 = []
for z in range(1,M):
    t.append(z*dt)
    for ž in range(1,N-1):
        u2.append(alfa*u[ž+1]+(1-2*alfa)*u[ž]+alfa*u[ž-1])
    u.clear()
    for đ in u2:
        u.append(đ)
    if z == 100:
        for h in u:
            u100.append(h)
    elif z == 200:
        for g in u:
            u200.append(g)
    elif z == 300:
        for f in u:
            u300.append(f)
    elif z == 400:
        for s in u:
            u400.append(s)
    u2.clear()
    u2.append(u[0])
    u.append(0)
x_dx = []
for š in range(1,N):
    x_dx.append(š*dx)
    x = š*dx
    if x > 20:
        break
plt.plot(x_dx,u0)
plt.plot(x_dx,u100)
plt.plot(x_dx,u200)
plt.plot(x_dx,u300)
plt.plot(x_dx,u400)
plt.xlabel("x [m]")
plt.ylabel("u [kg/m^3]")
plt.title("Implicitna metoda")
plt.legend(["t = 0","t = 100dt","t = 200dt","t = 300dt", "t = 400dt"])
plt.title("Eksplicitna metoda")
plt.show()
#implicitno
u100.clear()
u200.clear()
u300.clear()
u400.clear()
t.clear()
u.clear()
u2.clear()
u2 = []
for šš in range(1,N):
    x_lista.append(šš*dx)
    x = x_lista[šš-1]
    if x < 2:
        u.append(0)
x_lista.clear()
x_lista = [x0]
for dž in range(1,N):
    x_lista.append(dž*dx)
    x = x_lista[dž-1]
    if x >=2 and x<= 5:
        u.append(5.5)
x_lista.clear()
x_lista = [x0]
for o in range(1,N):
    x_lista.append(o*dx)
    x = x_lista[o]
    if x > 5:
        u.append(0)
u_0 = []
for mmf in u:
    u_0.append(mmf)
A1 = []
A2 = []
A3 = []
for i in range(0,N):
    A1.append(-alfa)
    A2.append(1+2*alfa)
    A3.append(-alfa)
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
for AA in range(1,M):
    t.append(AA*dt)
    u3 = thomas(A1,A2,A3,u,N)
    u.clear()
    for đđ in u3:
        u.append(đđ)
    if AA == 100:
        for hh in u:
            u100.append(hh)
    elif AA == 200:
        for gg in u:
            u200.append(gg)
    elif AA == 300:
        for ff in u:
            u300.append(ff)
    elif AA == 400:
        for ss in u:
            u400.append(ss) 
    u.append(0)
x_dx.clear()
for š in range(0,N):
    x_dx.append(š*dx)
    x = š*dx
    if x > 20:
        break
plt.plot(x_dx,u_0)
plt.plot(x_dx,u100)
plt.plot(x_dx,u200)
plt.plot(x_dx,u300)
plt.plot(x_dx,u400)
plt.xlabel("x [m]")
plt.ylabel("u [kg/m^3]")
plt.title("Implicitna metoda")
plt.legend(["t = 0","t = 100dt","t = 200dt","t = 300dt", "t = 400dt"])
plt.show()


        
     

        
        
