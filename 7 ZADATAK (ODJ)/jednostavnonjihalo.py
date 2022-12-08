import numpy
import matplotlib.pyplot as plt
def analiticki(y0,N=2000,l=0.2484902028828339,g=9.81):
    w0 = numpy.sqrt(g/l)
    T = 2*numpy.pi/w0
    x = []
    y = []
    for i in range(1,N):
        x.append(i*0.01)
        y.append(y0*numpy.cos(w0*x[i-1]))
    return x,y
def analiticki_period(l=0.2484902028828339,g=9.81):
    T = 2*numpy.pi*numpy.sqrt(l/g)
    return T
def funkcija(f,y):
    return f(y)
def f(y,t):
    return -((w0)**2)*numpy.sin(y)
def euler(y0,v0,t0=0,tN=20,N=2000,l=0.2484902028828339,g=9.81,fi_0=0):
    def funkcija(f,y):
        return f(y)
    def f(y,t):
        return -((w0)**2)*numpy.sin(y)
    w0 = numpy.sqrt(g/l)
    h = (tN-t0)/N
    y = [y0*numpy.pi/180]
    v = [v0]
    t = [t0]
    for i in range(1,N):
        t.append(t0+i*h)
        v.append(v[i-1] + f(y[i-1],t[i-1])*h)
        y.append(y[i-1] + v[i]*h)
    y_deg = []
    for j in y:
        y_deg.append(j*180/numpy.pi)
    return t,y_deg
def rk4(y0,v0,t0=0,tN=20,N=2000,l=0.2484902028828339,g=9.81,fi_0=0):
    def funkcija(f,y):
        return f(y)
    def f(y,t):
        return -((w0)**2)*numpy.sin(y)
    w0 = numpy.sqrt(g/l)
    h = (tN-t0)/N
    v_rk = [v0]
    y_rk = [y0*numpy.pi/180]
    t_rk = [t0]
    for k in range(1,N):
        t_rk.append(t_rk[k-1]+h)
        kv1 = f(y_rk[k-1],t_rk[k-1])
        ky1 = v_rk[k-1]
        kv2 = (f(y_rk[k-1]+ky1*h/2,t_rk[k-1]+h/2))
        ky2 = (v_rk[k-1]+kv1*h/2)
        kv3 = (f(y_rk[k-1]+ky2*h/2,t_rk[k-1]+h/2))
        ky3 = (v_rk[k-1]+kv2*h/2)
        kv4 = (f(y_rk[k-1]+ky3*h,t_rk[k]))
        ky4 = (v_rk[k-1]+kv3*h)
        v_rk.append(v_rk[k-1]+h*(kv1+2*kv2+2*kv3+kv4)/6)
        y_rk.append(y_rk[k-1]+h*(ky1+2*ky2+2*ky3+ky4)/6)
    y_rk_deg = []
    for q in y_rk:
        y_rk_deg.append(q*180/numpy.pi)
    return t_rk,y_rk_deg


